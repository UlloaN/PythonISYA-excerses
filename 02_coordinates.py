import numpy as np
import matplotlib.pyplot as plt

import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz


lmc_center = SkyCoord.from_name('M31') # search the object coordinate
lmc_center
new_ra=lmc_center.ra.hour  #to change to hour
new_dec=lmc_center.dec

# EarthLocation.get_site_names() to get a list of observatory
my_observatory = EarthLocation(lat=4.0*u.deg, lon=-75.0*u.deg, height=4000*u.m)
LCO = EarthLocation.of_site("Las Campanas Observatory")  #to download the coordinate datas of some telescope/observatory
LCO.lat, LCO.lon, LCO.height # to find latitud, longitud and heigh
print( LCO.lon,LCO.lat)

time = Time('2019-03-10 22:00:00') # That's in Universal Time Coordinated!
lmg_altaz = lmc_center.transform_to(AltAz(obstime=time,location=LCO))
print(lmg_altaz.az, lmg_altaz.alt) 


#Plot the altitude of M31 (the Andromeda galaxy) at Las Campanas Observatory on March 10th 2019 between 6PM and 6AM LOCAL TIME.
#Hint The following Python code is valid to get the time 30 minutes later than a given time and date.

#time = Time('2019-03-10 18:00:00') + 0.5*u.hour

#Will be M31 observable that night at Las Campanas? / asw: NO
