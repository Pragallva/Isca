import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os
#import sys

#dirc=sys.argv

ocean_file_name = os.getcwd()+'/ocean_zeroqflux.nc'
qflux_file = Dataset(ocean_file_name, 'r+', format='NETCDF3_CLASSIC')
v_var=qflux_file.variables
source_flux=v_var['ocean_qflux'][:]
lon=v_var['lon'][:]; nlon=len(lon)
#new_flux=np.squeeze(np.nanmean(source_flux,axis=2))
#zonal_flux = np.dstack([new_flux]*nlon)
zero_flux  = np.zeros(np.shape(source_flux))
v_var['ocean_qflux'][:] = zero_flux
qflux_file.close()

#vv=np.linspace(-250,250,100)
#plt.contourf(lons,lats, zonal_flux[dirc[1],:,:],vv);plt.colorbar()
#plt.show()

print zero_flux.shape
    
