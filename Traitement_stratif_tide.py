#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:01:37 2020

@author: koealaquillage
"""

#*********************************#
# Script to observe the stratifi- #
# tion in the curents of Ouano    #
# By G. Koenig, the 17/11/2020    #
# Here I measure the tidal        #
# Currents                        #
#*********************************#

#*******Packages import***********#
#***Packages import**********#
import numpy as np
from scipy import io
import scipy.interpolate
import utide
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse,Rectangle
#*****Useful functions************#
def import_data_Cristele(eta_data) :
    """ Function to import the data from the matlab files of Cristele.
    INPUTS :
    eta_data : Dataframe of the .mat file
    OUTPUTS :
    data_frame : Dataframe with the date, the longitude or latitude positions and
    the pressure"""
    
    # We load data from the Matlab files "
    eta=scipy.io.loadmat(eta_data)
    # Now we format the time, so that it is easier to read #
    
    df = pd.DataFrame({'year':eta['Temps']['year'][0][0][:,0],
                  'month':eta['Temps']['month'][0][0][:,0],
                   'day':eta['Temps']['day'][0][0][:,0],
                    'hour':eta['Temps']['hour'][0][0][:,0],
                    'minute':eta['Temps']['minute'][0][0][:,0],
                     'second':eta['Temps']['year'][0][0][:,0]})
    
    
    return pd.DataFrame({'Latitude' : eta['P'][0,0][0][0][0],
                          'Longitude' : eta['P'][0,0][1][0][0],
                          'Depth_surf' : eta['P'][0,0][2][:,0],
                          'Depth_1' : eta['P_Adcp'][0][0][0][0][0],
                          'Depth_2' : eta['P_Adcp'][0][0][0][0][1],
                          'Depth_3' : eta['P_Adcp'][0][0][0][0][2],
                          'Depth_4' : eta['P_Adcp'][0][0][0][0][3],
                          'Depth_5' : eta['P_Adcp'][0][0][0][0][4],
                          'Depth_6' : eta['P_Adcp'][0][0][0][0][5],
                          'Depth_7' : eta['P_Adcp'][0][0][0][0][6],
                          'Depth_8' : eta['P_Adcp'][0][0][0][0][7],
                          'Depth_9' : eta['P_Adcp'][0][0][0][0][8],
                          'Depth_10' : eta['P_Adcp'][0][0][0][0][9],
#                          'Depth_11' : eta['P_Adcp'][0][0][10][:],
#                          'Depth_12' : eta['P_Adcp'][0][0][11][:],
#                          'Depth_11' : eta['P_Adcp'][0][0][12][:],
                          'U_1': eta['vitesse'][0][0][0][:,0],
                          'U_2': eta['vitesse'][0][0][0][:,1],
                          'U_3': eta['vitesse'][0][0][0][:,2],
                          'U_4': eta['vitesse'][0][0][0][:,3],
                          'U_5': eta['vitesse'][0][0][0][:,4],
                          'U_6': eta['vitesse'][0][0][0][:,5],
                          'U_7': eta['vitesse'][0][0][0][:,6],
                          'U_8': eta['vitesse'][0][0][0][:,7],
                          'U_9': eta['vitesse'][0][0][0][:,8],
                          'U_10': eta['vitesse'][0][0][0][:,9],
#                          'U_11': eta['vitesse'][0][0][0][:,10],
#                          'U_12': eta['vitesse'][0][0][0][:,11],
#                          'U_13': eta['vitesse'][0][0][0][:,12],
#                          'U_14': eta['vitesse'][0][0][0][:,13],
#                          'U_15': eta['vitesse'][0][0][0][:,14],
#                          'U_16': eta['vitesse'][0][0][0][:,15],
#                          'U_17': eta['vitesse'][0][0][0][:,16],
#                          'U_18': eta['vitesse'][0][0][0][:,17],
#                          'U_19': eta['vitesse'][0][0][0][:,18],
#                         'U_20': eta['vitesse'][0][0][0][:,19],
#                          'U_21': eta['vitesse'][0][0][0][:,20],
                          'V_1': eta['vitesse'][0][0][1][:,0],
                          'V_2': eta['vitesse'][0][0][1][:,1],
                          'V_3': eta['vitesse'][0][0][1][:,2],
                          'V_4': eta['vitesse'][0][0][1][:,3],
                          'V_5': eta['vitesse'][0][0][1][:,4],
                          'V_6': eta['vitesse'][0][0][1][:,5],
                          'V_7': eta['vitesse'][0][0][1][:,6],
                          'V_8': eta['vitesse'][0][0][1][:,7],
                          'V_9': eta['vitesse'][0][0][1][:,8],
                          'V_10': eta['vitesse'][0][0][1][:,9],
#                          'V_11': eta['vitesse'][0][0][1][:,10],
#                          'V_12': eta['vitesse'][0][0][1][:,11],
#                          'V_13': eta['vitesse'][0][0][1][:,12],
#                          'V_14': eta['vitesse'][0][0][1][:,13],
#                          'V_15': eta['vitesse'][0][0][1][:,14],
#                          'V_16': eta['vitesse'][0][0][1][:,15],
#                          'V_17': eta['vitesse'][0][0][1][:,16],
#                          'V_18': eta['vitesse'][0][0][1][:,17],
#                          'V_19': eta['vitesse'][0][0][1][:,18],
#                          'V_20': eta['vitesse'][0][0][1][:,19],
#                          'V_21': eta['vitesse'][0][0][1][:,20],
                          },index=pd.to_datetime(df))
    
       
       
#*******Now I define the paths to the data and the data I want to see
# List of station
       
# The data position
path_data = '/media/koealaquillage/LaCie/Donnees_NC/Pour_Guillaume/'\
            +'Courant_Donnees/DonneesPropres/'
            
data_file = 'Vit_PDigo.mat'

# The dictionnary to store data
dic_stat = []

# A variable for the time as well
time_tide=[]

# A list to store the different coefficient
list_coeff = []

#*******Now I try and import it*********#
dic_stat = import_data_Cristele(path_data+data_file)

#******Now we want to get the tides out of it
time = (dic_stat.index.view('int64')//60000000000.)/1440. # We must give time inputs in days

for i in range (6) :
    coeff = utide.solve(time,dic_stat['U_'+str(i+1)].values,dic_stat['V_'+str(i+1)].values,lat=dic_stat['Latitude'][0],
                        nodal=True,trend=True,method='robust',conf_int='linear',
                         Rayleigh_min=.95)
    list_coeff.append(coeff)
    
#*** And if I try the plotting
fig, ax = plt.subplots()

# A stuff for the colors#
cmap = plt.cm.coolwarm

# I plot a first reference ellipse
ell_ref = Ellipse(xy=[115,-5.2], width= 0., height=1.,angle = 145.,
                  edgecolor = 'black',fill=False)
ax.add_patch(ell_ref)

# And the indicative text
ax.text(115, -5.9, '10 cm.s-1 \n 145 degrees',
         horizontalalignment='center', verticalalignment='bottom')
for i in range(5) :
    depth = -dic_stat['Depth_surf'].mean() + dic_stat['Depth_'+str(i+1)].mean()
    ell = Ellipse(xy=[list_coeff[i]['g'][0],depth], width=list_coeff[i]['Lsmin'][0]/100., 
                  height=list_coeff[i]['Lsmaj'][0]/100., 
                  angle = list_coeff[i]['theta'][0],label = 'Level'+str(i+1),
                  edgecolor = cmap(5./(4.*i+0.01)),fill=False)
    
    ax.add_patch(ell)

# We add some labels
ax.set_ylabel('Depth (m)')
ax.set_xlabel('Phase (degrees)')
ax.set_title('M2 tidal ellipses')

ax.autoscale()
plt.show()
