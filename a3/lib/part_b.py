from Plotter import *

e_rate = {}
e_rate[0.25] = 0.278
e_rate[0.5] = 0.220
e_rate[1] = 0.156
e_rate[2] = 0.090
e_rate[4] = 0.037
e_rate[8] = 0.009
e_rate[16] = 0
e_rate[32] = 0
e_rate[64] = 0

v_rate = {}
v_rate[0.25] = 0.333
v_rate[0.5] = 0.298
v_rate[1] = 0.264
v_rate[2] = 0.236
v_rate[4] = 0.221
v_rate[8] = 0.205
v_rate[16] = 0.219
v_rate[32] = 0.216
v_rate[64] = 0.216


plot_multiline('part_b', [e_rate, v_rate], xlabel='', ylabel='', title='', labels=['Training','Validation'], xlog=2)