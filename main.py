#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from fastapi import FastAPI

app = FastAPI()
vehicle = pd.read_csv(r'pertambahan-jumlah-kendaraan-bermotor-7-tahun-terakhir-2008-2014-wilayah-jakarta-depok-tangerang-bekasi.csv')
vhcl = pd.DataFrame(vehicle)

@app.get('/')
def read_root():
    profile = ['API Assignment',
            '',
            'Nama: Hanan Suryandhito', 
            'NPK: 67688']
    link = ['Coba path: ',
            '/data untuk data,',
            '/1st_analysis,', 
            '/2nd_analysis, dan', 
            '/3rd_analysis untuk analysis.']
    return {'profile':profile, 'Instructions':link}

@app.get('/data')
def read_data():
    vhcl
    return {'Data':vhcl}

@app.get('/1st_analysis/')
def read_first():
    mobpy = vhcl['pertambahan_mobil_per tahun']
    mobrow = mobpy.iloc[0:6]
    mobsummed = mobrow.sum()
    printsummob = 'Dari 2008 - 2013 (Untuk sementara 2014 dianggap outlier), jumlah mobil di Jakarta, Depok, Tangerang, dan Bekasi meningkat sebesar:'
    first_analysis='Perubahan jumlah mobil di Jakarta, Depok, Tangerang, dan Bekasi dari tahun 2008 terus naik dan memuncak di tahun 2013'
    return {'Data':mobpy, 'First analysis':first_analysis, 'printmob':printsummob, 'mobsummed':mobsummed}

@app.get('/2nd_analysis/')
def read_second():
    motpy = vhcl['pertambahan_motor_per tahun']
    motrow = motpy.iloc[0:6]
    motsummed = motrow.sum()
    printsummot = 'Dari 2008 - 2013 (Untuk sementara 2014 dianggap outlier), jumlah motor di Jakarta, Depok, Tangerang, dan Bekasi meningkat sebesar:'
    second_analysis='Perubahan jumlah motor di Jakarta, Depok, Tangerang, dan Bekasi dari tahun 2008 terus naik dan memuncak di tahun 2013'
    return {'Data':motpy, 'Second analysis':second_analysis, 'printmot':printsummot, 'motsummed':motsummed}

@app.get('/3rd_analysis/')
def read_third():
    mmph = vhcl[['tahun','pertambahan_mobil_per tahun','pertambahan_motor_per tahun']]
    mmphrate = mmph.iloc[0:6]
    mmphr = mmphrate.drop(columns='tahun')
    rate = mmphr.mean()
    third_analysis='Kenaikan jumlah mobil dan motor rata-rata per tahun adalah: '
    return {'Data':mmph, 'Third_analysis':third_analysis, 'rata':rate}

