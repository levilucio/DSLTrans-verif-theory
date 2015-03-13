#!/usr/bin/env python

import pickle
import numpy
import pylab
import sys

from convert import *

number_of_rules = [3, 5, 7, 10, 12, 14, 17, 19, 21]
number_of_pcs = [8,	16,	34,	272,	442,	1156,	9248,	15028,	39304]
time_to_build = [0.003,	0.13,	0.39,	1.87,	2.68,	9.00,	59.08,	97.52,	369.19]
mem_size = [0.08,	0.09,	0.17,	1.24,	1.83,	4.98,	38.01,	60.10,	156.79]
time_prop_1= [	0, 0.19,	1.26,	2.4,	3.4,	8.38,	73.51,	140.77,	412.02]

time_prop_2=[	0.003, 0.003,	0.003,	0.003,	0.003,	0.003,	0.003,	0.003,	0.003]



from matplotlib.ticker import ScalarFormatter 
majorFormatter = ScalarFormatter()


font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 22}

pylab.rc('font', **font)

#num rules vs num PCs
#fig, ax = pylab.subplots()

pylab.hold('off')
#fig=pylab.semilogy(number_of_rules, number_of_pcs)
##pylab.hold('on')




pylab.clf()

# NUM RULES VS MEMORY



fig=pylab.loglog(number_of_pcs, time_prop_1)
#pylab.hold('on')

pylab.xlim([8,39304])

#pylab.hold('on')
#title = "Num rules vs PCs"
filename = "pcs_vs_prop1"+ ".svg"

pylab.xlabel("Number of path conditions")
pylab.ylabel("Time (s)")
#pylab.legend(legend, 'upper left')
#pylab.title(title)


pylab.savefig(filename, format = "svg", transparent=True, bbox_inches='tight', pad_inches=0.05)

convert("./" + filename)



pylab.clf()

# NUM RULES VS MEMORY



#fig=pylab.semilogx(number_of_pcs, time_prop_2)
##pylab.hold('on')

#pylab.xlim([8,39304])

##pylab.hold('on')
##title = "Num rules vs PCs"
#filename = "pcs_vs_prop2"+ ".svg"

#pylab.xlabel("Number of path conditions")
#pylab.ylabel("Time (s)")
##pylab.legend(legend, 'upper left')
##pylab.title(title)
#pylab.savefig(filename, format = "svg", transparent=True, bbox_inches='tight', pad_inches=0.05)

#convert("./" + filename)


