#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:23:03 2020

@author: koealaquillage
"""

#*********************************#
# Script to observe the stratifi- #
# tion in the curents of Ouano    #
# By G. Koenig, the 17/11/2020    #
# I added some smoothing          #
#*********************************#

#*******Packages import***********#
#***Packages import**********#
import numpy as np
from scipy import io
import scipy.interpolate
import utide
import pandas as pd
import matplotlib.pyplot as plt
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
                          'Depth' : eta['P'][0,0][2][:,0],
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
    
#def tidal_filtering(time,zeta,lat):
#    """" Here we want to extract the M2 harmonic from a signal :
        
#        INPUTS:
#        time : The time serie in days
#        zeta : The elevation in m
#        lat : the latitude
        
#        OUTPUTS :
#        the coefficients of tides""""
        
#         Time=(Dict_Stations[BAR].index.view('int64')//pd.Timedelta(1,unit='m'))/1440. # We must give time inputs in days
#        coeff=utide.solve(time,zeta[:,i,j],lat=lat[i,j],nodal=True,
#                          trend=True,method='robust',conf_int='linear',
#                          Rayleigh_min=.95)
        # And I extract M2 coefficients for example
#        amp_M2[i,j]=Coeff['A'][0]
#        phase_M2[i,j]=Coeff['g'][0]
       
        # And we return
#        return amp_M2, phase_M2
       
       
#*******Now I define the paths to the data and the data I want to see
# List of station
       
# The data position
path_data = '/media/koealaquillage/LaCie/Donnees_NC/Pour_Guillaume/'\
            +'Courant_Donnees/DonneesPropres/'
            
data_file = 'Vit_PDigo.mat'

# The dictionnary to store data
dic_stat = []

# The plot for U
fig_U = plt.figure()
ax_U = fig_U.add_subplot()

# And for V
fig_V = plt.figure()
ax_V = fig_V.add_subplot()



#*******Now I try and import it*********#
dic_stat = import_data_Cristele(path_data+data_file)


# ANd now I plot it *****#
#
for i in range(6) :
   ax_U.plot(dic_stat['U_'+str(1+i)].ewm(span=5000).mean(),label='Level '+str(1+i))

#ax_U.plot(dic_stat['U_1'].ewm(span=7000).mean(),label='Level 1')
#ax_U.plot(dic_stat['U_14'].ewm(span=7000).mean(),label='Level 14')

ax_U.legend(loc='best')
ax_U.set_ylabel('Velocity (mm.s-1)')
ax_U.set_xlabel('Date')

for i in range(6) :
   ax_V.plot(dic_stat['V_'+str(1+i)].ewm(span=5000).mean(),label='Level '+str(1+i))

#ax_V.plot(dic_stat['V_1'].ewm(span=7000).mean(),label='Level 1')
#ax_V.plot(dic_stat['V_14'].ewm(span=7000).mean(),label='Level 14')

ax_V.legend(loc='best')
ax_V.set_ylabel('Velocity (mm.s-1)')
ax_V.set_xlabel('Date')
