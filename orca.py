import iris
import matplotlib.pyplot as plt
import numpy as np
import iris.quickplot as qplt

orca = iris.load('/nesi/project/niwa00013/tids/OCEAN/hadgem3/ancil/ocean/eORCA1/MEDUSA/eORCA1_dust.nc')

lats = orca[1]
lons = orca[2]

print(orca)

qplt.pcolormesh(lats)

plt.savefig('./lats.png')
