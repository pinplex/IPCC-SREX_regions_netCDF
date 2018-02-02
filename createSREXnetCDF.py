#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 09:56:22 2018
@author: alexander.winkler@mpimet.mpg.de
Title: SREX regions netcdf
"""

## import modules
import regionmask
print regionmask.__version__

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

import time

## define resolution in degree
lon_res = 1.875
lat_res = 1.875

## specify resolutions
lon = np.arange(-180, 180, lon_res)
lat = np.arange(-90, 90, lat_res)

## create dataset
ds = xr.Dataset(coords={'lon': lon,
                        'lat': lat,})

## define the srex regions
ds = regionmask.defined_regions.srex.mask(ds).to_dataset()

## attach attribute information
abbrevs = regionmask.defined_regions.srex.abbrevs
names = regionmask.defined_regions.srex.names
numbers = regionmask.defined_regions.srex.numbers

description = 'Region ID - Abbrevation - Longname; '

for i in range(len(numbers)):
    description += str(numbers[i])+' - '+str(abbrevs[i])+' - '+str(names[i])+'; '

ds.attrs['title'] = 'IPCC SREX regions mask'
ds.attrs['history'] = 'Created on ' + time.ctime()
ds.attrs['createor_email'] = 'alexander.winkler@mpimet.mpg.de'
ds.attrs['source'] = 'Seneviratne et al., 2012 (https://www.ipcc.ch/pdf/special-reports/srex/SREX-Ch3-Supplement_FINAL.pdf) and python module regionmask (http://regionmask.readthedocs.io/en/stable/index.html)'

ds.attrs['projection'] = 'lonlat'
ds.attrs['geospatial_lat_resolution'] = str(lat_res)+' deg'
ds.attrs['geospatial_lon_resolution'] = str(lon_res)+' deg'
ds.attrs['geospatial_lat_min'] = -90
ds.attrs['geospatial_lat_max'] = 90
ds.attrs['geospatial_lon_min'] = -180
ds.attrs['geospatial_lon_max'] = 180

ds.attrs['comment'] = description

## store to file
ds.to_netcdf('SREX_regions_mask_'+str(lon_res)+'x'+str(lat_res)+'.nc')

## print description
print description.replace(';', '\n')

## make plot showing different regions
plt.figure()
regionmask.defined_regions.srex.plot()
plt.title('IPCC SREX Regions')
