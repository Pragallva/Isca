import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os
#import sys

#dirc=sys.argv

ocean_file_name = os.getcwd()+'/ocean_qflux.nc'
qflux_file = Dataset(ocean_file_name, 'r+', format='NETCDF3_CLASSIC')
v_var=qflux_file.variables
source_flux=v_var['tracmip_qflux'][:]
new_flux=np.squeeze(np.nanmean(source_flux,axis=1))


lats=v_var['lat'][:]; nlat=len(lats)
lons=v_var['lon'][:]; nlon=len(lons)
latbs=v_var['latb'][:]; nlatb=len(latbs)
lonbs=v_var['lonb'][:]; nlonb=len(lonbs)
#zonal_flux = np.dstack([new_flux]*nlon)
#zero_flux  = np.zeros(np.shape(source_flux))

#zero_flux_netcdf  = qflux_file.createVariable('ocean_zeroqflux','f4',('time','lat','lon',)) 
#zonal_flux_netcdf = qflux_file.createVariable('ocean_zonalqflux','f4',('time','lat','lon',))
#tracmip_flux_netcdf = qflux_file.createVariable('tracmip_qflux','f4',('lat','lon',))
#zonal_tracmip_flux_netcdf = qflux_file.createVariable('zonal_tracmip_qflux','f4',('lat','lon',))
tracmip_flux_new_netcdf = qflux_file.createVariable('tracmip_qflux_new','f4',('time','lat','lon',))

tracmip_add_time_dim = np.dstack([source_flux]*12)
tracmip_add_time_dim = tracmip_add_time_dim.transpose(2,0,1)

tracmip_flux_new_netcdf[:]=tracmip_add_time_dim
#zonal_tracmip_flux = np.load(os.getcwd()+'/zonal_tracmip_qflux.npy')
#zonal_flux = np.squeeze( np.dstack([zonal_tracmip_flux]*nlon) )

#zero_flux_netcdf[:] = zero_flux
#zonal_flux_netcdf[:] = zonal_flux  #zonal_flux --> This creates a zonal qflux
#tracmip_flux_netcdf[:] = tracmip_flux

#v_var['tracmip_qflux'][:]=tracmip_flux
#v_var['zonal_tracmip_qflux'][:]=zonal_flux

qflux_file.close()

#vv=np.linspace(-250,250,100)
#plt.contourf(lons,lats, zonal_flux[dirc[1],:,:],vv);plt.colorbar()
#plt.show()

#print zonal_flux.shape
    
