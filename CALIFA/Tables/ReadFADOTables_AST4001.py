#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 08:30:06 2020

@author: jean
"""

from __future__ import print_function, division, absolute_import

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Read FADO output tables in list format
# AST4001

# Read SampleStatistics file

# SampleStatistics_lista_SDSS_CALIFA.txt.table
# SampleEmissionEL_lista_SDSS_CALIFA.txt.table

FluxUnit = 1.e-17
file_stats = 'SampleStatistics_lista_SDSS_CALIFA.txt.table'
file_emlin = 'SampleEmissionEL_lista_SDSS_CALIFA.txt.table'

# Read first Statistics file
f = open(file_stats, "r")
count_lines = len(open(file_stats).readlines( ))

print("# of lines in the statistics file are: {}".format(count_lines))
        
spectrum = [] #00 -> Spectrum
galsnorm = [] #03 -> Normalization
L_DisMpc = [] #04 -> Luminosity distance in Mpc
Gnebular = [] #10 -> Nebular extinction
GnebBdev = [] #12 -> Nebular extinction error

bstLLage = [] #31 -> Mean stellar age light-weighted
devLLage = [] #33 -> Mean stellar age light-weighted error
bstLMage = [] #34 -> Mean stellar age mass-weighted
devLMage = [] #36 -> Mean stellar age mass-weighted error

bst_Lmet = [] #37 -> Mean stellar metallicity light-weighted
dev_Lmet = [] #39 -> Mean stellar metallicity light-weighted

logMEbst = [] #43 -> log of stellar mass ever formed
logMEdev = [] #45 -> log of stellar mass ever formed error

logMCbst = [] #46 -> log of stellar mass corrected for ism return
logMCdev = [] #48 -> log of stellar mass corrected for ism return error

FObst_Ha = [] #85 -> Halpha flux
FOdev_Ha = [] #87 -> Error of Halpha flux
EObst_Ha = [] #88 -> Halpha equivalent width
EOdev_Ha = [] #90 -> Error of the  Halpha equivalent width

FObst_Hb = [] #91 -> Hbeta flux
FOdev_Hb = [] #93 -> Error of Hbeta flux
EObst_Hb = [] #94 -> Hbeta equivalent width
EOdev_Hb = [] #96 -> Error of the  Hbeta equivalent width

for line in f:
    line    = line.strip()
    columns = line.split()
    #name    = columns[2]
    #j       = float(columns[3])
    #print(name, j)
    if columns[1] == 'spectrum':
        col_names = columns
        print(repr(col_names))
    
    string = columns[0]
    if string[0:1] != '#':
        spectrum.append(columns[0]) #00
        galsnorm.append(columns[3]) #03
        L_DisMpc.append(columns[4]) #04
        Gnebular.append(columns[10]) #10
        GnebBdev.append(columns[12]) #12
        
        bstLLage.append(columns[31]) #31
        devLLage.append(columns[33]) #33
        bstLMage.append(columns[34]) #34
        devLMage.append(columns[36]) #36
        
        bst_Lmet.append(columns[37]) #37
        dev_Lmet.append(columns[39]) #39
        
        logMEbst.append(columns[43]) #43
        logMEdev.append(columns[45]) #45
        
        logMCbst.append(columns[46]) #46
        logMCdev.append(columns[48]) #48
        
        FObst_Ha.append(columns[85]) #85
        FOdev_Ha.append(columns[87]) #87
        EObst_Ha.append(columns[88]) #88
        EOdev_Ha.append(columns[90]) #90
        
        FObst_Hb.append(columns[91]) #91
        FOdev_Hb.append(columns[93]) #93
        EObst_Hb.append(columns[94]) #94
        EOdev_Hb.append(columns[96]) #96
       
# Convert to numpy arrays
galsnorm = np.array(galsnorm, dtype='float')
L_DisMpc = np.array(L_DisMpc, dtype='float')
Gnebular = np.array(Gnebular, dtype='float')
GnebBdev = np.array(GnebBdev, dtype='float')
        
bstLLage = np.array(bstLLage, dtype='float')
devLLage = np.array(devLLage, dtype='float')
bstLMage = np.array(bstLMage, dtype='float')
devLMage = np.array(devLMage, dtype='float')
        
bst_Lmet = np.array(bst_Lmet, dtype='float')
dev_Lmet = np.array(dev_Lmet, dtype='float')
        
logMEbst = np.array(logMEbst, dtype='float')
logMEdev = np.array(logMEdev, dtype='float')
        
logMCbst = np.array(logMCbst, dtype='float')
logMCdev = np.array(logMCdev, dtype='float')
        
FObst_Ha = np.array(FObst_Ha, dtype='float')
FOdev_Ha = np.array(FOdev_Ha, dtype='float')
EObst_Ha = np.array(EObst_Ha, dtype='float')
EOdev_Ha = np.array(EOdev_Ha, dtype='float')
        
FObst_Hb = np.array(FObst_Hb, dtype='float')
FOdev_Hb = np.array(FOdev_Hb, dtype='float')
EObst_Hb = np.array(EObst_Hb, dtype='float')
EOdev_Hb = np.array(EOdev_Hb, dtype='float')
        
bst_Lmet = np.array(bst_Lmet, dtype='float')
bst_Lmet = np.log10(bst_Lmet/0.02)

f.close()

print(" ")

# Read secondly the Emission-line file
# EL_____1[NeV]    3425.50000      0001--0021               
# EL_____2[OII]    3727.00000      0022--0042               
# EL_____3[OII]    3729.00000      0043--0063               
# EL_____4H12      3750.20000      0064--0084               
# EL_____5H11      3770.60000      0085--0105               
# EL_____6H10      3797.90000      0106--0126               
# EL_____7H9       3835.40000      0127--0147               
# EL_____8[NeIII]  3869.10000      0148--0168               
# EL_____9H8HeI    3889.00000      0169--0189               
# EL____10[NeIII]  3967.80000      0190--0210               
# EL____11Hepsilon 3970.10000      0211--0231               
# EL____12HeI      4026.20000      0232--0252               
# EL____13[SII]    4068.60000      0253--0273               
# EL____14[SII]    4076.30000      0274--0294               
# EL____15Hdelta   4101.70000      0295--0315               
# EL____16Hgamma   4340.50000      0316--0336               
# EL____17[OIII]   4363.20000      0337--0357               
# EL____18HeI      4471.50000      0358--0378               
# EL____19[FeIII]  4658.00000      0379--0399               
# EL____20HeII     4685.70000      0400--0420               
# EL____21[ArIV]   4711.40000      0421--0441               
# EL____22HeI      4713.20000      0442--0462               
# EL____23[ArIV]   4740.20000      0463--0483               
# EL____24Hbeta    4861.30000      0484--0504               
# EL____25HeI      4921.90000      0505--0525               
# EL____26[OIII]   4958.90000      0526--0546               
# EL____27[FeVII]  4988.60000      0547--0567               
# EL____28[OIII]   5006.80000      0568--0588               
# EL____29HeI      5015.70000      0589--0609               
# EL____30[FeVII]  5158.40000      0610--0630               
# EL____31[NI]     5199.10000      0631--0651               
# EL____32[FeIII]  5270.40000      0652--0672               
# EL____33[ClIII]  5519.20000      0673--0693               
# EL____34[NII]    5754.60000      0694--0714               
# EL____35HeI      5875.60000      0715--0735               
# EL____36[FeVII]  6086.30000      0736--0756               
# EL____37[OI]     6300.30000      0757--0777               
# EL____38[SIII]   6312.10000      0778--0798               
# EL____39[OI]     6363.80000      0799--0819               
# EL____40[NII]    6548.00000      0820--0840               
# EL____41Halpha   6562.80000      0841--0861               
# EL____42[NII]    6583.50000      0862--0882               
# EL____43HeI      6678.20000      0883--0903               
# EL____44[SII]    6716.40000      0904--0924               
# EL____45[SII]    6730.80000      0925--0945               
# EL____46HeI      7065.20000      0946--0966               
# EL____47[ArIII]  7135.80000      0967--0987               
# EL____48[OII]    7319.50000      0988--1008               
# EL____49[OII]    7330.20000      1009--1029               
# EL____50[ArIII]  7751.10000      1030--1050               
# EL____51[FeII]   8617.00000      1051--1071

# Only this lines are necessary
# EL____24Hbeta    4861.30000
# EL____28[OIII]   5006.80000
# EL____41Halpha   6562.80000              
# EL____42[NII]    6583.50000

EL_flux_Hbeta  = [] # Flux of Hbeta
EL_flux_OIII   = [] # Flux of [OIII] 5007
EL_flux_Halpha = [] # Flux of Halpha
EL_flux_NII    = [] # Flux of [NII] 6584

EL_fluxerror_Hbeta = [] # Flux error of Hbeta
EL_fluxerror_OIII   = [] # Flux error of [OIII] 5007
EL_fluxerror_Halpha = [] # Flux error of Halpha
EL_fluxerror_NII    = [] # Flux error of [NII] 6584

f = open(file_emlin, "r")
count_lines = len(open(file_emlin).readlines( ))

print("# of lines in the emission-line file are: {}".format(count_lines))
for i in enumerate(f):
    line    = i[1].strip()
    columns = line.split()
    
    string = columns[0]
    if string[0:1] != '#':
        #col_names = columns
        #print(np.size(columns))
        
        EL_flux_Hbeta.append(columns[1+4*23])
        EL_flux_Halpha.append(columns[1+4*40])
        EL_flux_OIII.append(columns[1+4*27])
        EL_flux_NII.append(columns[1+4*41])
        
        EL_fluxerror_Hbeta.append(columns[2+4*23])
        EL_fluxerror_Halpha.append(columns[2+4*40])
        EL_fluxerror_OIII.append(columns[2+4*27])
        EL_fluxerror_NII.append(columns[2+4*41])
        print(columns)
        
EL_flux_Hbeta = np.array(EL_flux_Hbeta, dtype='float')
EL_flux_Halpha = np.array(EL_flux_Halpha, dtype='float')
EL_flux_OIII = np.array(EL_flux_OIII, dtype='float')
EL_flux_NII = np.array(EL_flux_NII, dtype='float')

EL_fluxerror_Hbeta = np.array(EL_fluxerror_Hbeta, dtype='float')
EL_fluxerror_Halpha = np.array(EL_fluxerror_Halpha, dtype='float')
EL_fluxerror_OIII = np.array(EL_fluxerror_OIII, dtype='float')
EL_fluxerror_NII = np.array(EL_fluxerror_NII, dtype='float')

f.close()
    
    
# Example of plot
fig, ax = plt.subplots()
ax.scatter(logMCbst,bstLLage)

ax.set(xlabel='', ylabel='',
       title='log of stellar Mass versus Mean Stellar Age')
ax.grid()

#fig.savefig("test.png")
plt.show()

# Example of plot
fig, ax = plt.subplots()
OIII_Hb = EL_flux_OIII/EL_flux_Hbeta
NII_Ha = EL_flux_NII/EL_flux_Halpha
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,1.5)

ax.scatter(np.log10(abs(NII_Ha)),np.log10(abs(OIII_Hb)))