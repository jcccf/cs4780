from Plotter import *

# These are reversed!

idx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
v = [621, 470, 256, 140, 162, 68, 112, 58, 16, 26, 16, 12, 2, 0, 0, 0, 0, 0, 0, 0]
v = [float(x)/1000 for x in v]
v_rate = dict(zip(idx,v))


e = [442, 258, 227, 222, 233, 236, 220, 219, 225, 222, 228, 219, 227, 227, 227, 227, 227, 227, 227, 227]
e = [float(x)/1000 for x in e]
e_rate = dict(zip(idx,e))

plot_multiline('part_a', [v_rate, e_rate], xlabel='', ylabel='', title='', labels=['Training','Validation'])