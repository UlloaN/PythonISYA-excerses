import numpy as np
import matplotlib.pyplot as plt

import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz


lmc_center = SkyCoord.from_name('M31')
lmc_center
new_ra=lmc_center.ra.hour
new_dec=lmc_center.dec
