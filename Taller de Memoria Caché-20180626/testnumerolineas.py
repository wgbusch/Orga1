from cache import *

import numpy as np

import pylab

dom = [1,2,4,8,16,32,64]

res = []

for l in dom:
	c = CacheCorrespondenciaDirecta(memory = range(0,2**16), cacheSize = 128, nLines = l)
	c.fetchFrom('benchmark.list')
	res.append( c.hitRate() )
	print("Lineas: ",l,"HitRate: ",c.hitRate() )
pylab.plot(dom, res,'.-',lw=2,label='CacheCorrespondenciaDIrecta - FIFO')
pylab.xticks(size=16)
pylab.yticks(size=16)
pylab.xlim([0,np.max(dom)])
pylab.xlabel('lineas', size=16) 
pylab.ylabel('Hit Rate',size=16)
pylab.title('Cache Correspondencia Directa', size=16)
pylab.show()
