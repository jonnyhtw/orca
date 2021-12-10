import iris
import matplotlib.pyplot as plt
import numpy as np
import iris.quickplot as qplt

fig = plt.figure()

plt.ion()

dust = iris.load('/nesi/project/niwa00013/tids/OCEAN/hadgem3/ancil/ocean/eORCA1/MEDUSA/eORCA1_dust.nc')
print(dust)

radiation = iris.load('/nesi/project/niwa00013/tids/OCEAN/hadgem3/forcing/ocean/eORCA1/GA7_PI/ac310_rad_y2020m06.nc')
print(radiation)


lats = dust[1]
lons = dust[2]

ax = plt.subplot(2,2,1)
qplt.pcolormesh(lats)
ax = plt.subplot(2,2,2)
qplt.pcolormesh(lons)
ax = plt.subplot(2,2,3)
qplt.pcolormesh(radiation[0][0])

plt.tight_layout()

#plt.show();

plt.savefig('./lats.png')
