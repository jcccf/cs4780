from Plotter import *

# This is actually the validation error
e_rate = {}
e_rate[1] = 0.408
e_rate[2] = 0.277
e_rate[3] = 0.491
e_rate[4] = 0.216
e_rate[5] = 0.248
e_rate[6] = 0.225
e_rate[7] = 0.215
e_rate[8] = 0.223
e_rate[9] = 0.220
e_rate[10] = 0.225
e_rate[11] = 0.226
e_rate[12] = 0.225
e_rate[13] = 0.221
e_rate[14] = 0.222
e_rate[15] = 0.217
e_rate[16] = 0.217
e_rate[17] = 0.217
e_rate[18] = 0.217
e_rate[19] = 0.217
e_rate[20] = 0.217

#[609, 470, 311, 165, 146, 130, 42, 36, 10, 18, 4, 8, 4, 2, 4, 0, 0, 0, 0, 0]

# Here v_rate is actually the training error
v_rate = {}
v_rate[1] = 0.609
v_rate[2] = 0.470
v_rate[3] = 0.311
v_rate[4] = 0.165
v_rate[5] = 0.146
v_rate[6] = 0.130
v_rate[7] = 0.042
v_rate[8] = 0.036
v_rate[9] = 0.010
v_rate[10] = 0.018
v_rate[11] = 0.004
v_rate[12] = 0.008
v_rate[13] = 0.004
v_rate[14] = 0.002
v_rate[15] = 0.004
v_rate[16] = 0
v_rate[17] = 0
v_rate[18] = 0
v_rate[19] = 0
v_rate[20] = 0

plot_multiline('part_a', [v_rate, e_rate], xlabel='', ylabel='', title='', labels=['Training','Validation'])