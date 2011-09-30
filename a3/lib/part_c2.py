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

def freadnumbers(filename):
  nums = []
  with open(filename,'r') as f:
    for l in f:
      nums.append(float(l.replace('\n','')))
  return nums

ns = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
val_1 = freadnumbers('../data/partc/tron_re1_all2.txt')
val_2 = freadnumbers('../data/partc/tron_re2_all2.txt')
val_3 = freadnumbers('../data/partc/tron_re3_all2.txt')
tra_1 = freadnumbers('../data/partc/tron_re1_all.txt')
tra_2 = freadnumbers('../data/partc/tron_re2_all.txt')
tra_3 = freadnumbers('../data/partc/tron_re3_all.txt')
tra_1 = [float(x)/1000 for x in tra_1]
tra_2 = [float(x)/1000 for x in tra_2]
tra_3 = [float(x)/1000 for x in tra_3]

val_1_dict = dict(zip(ns,val_1))
val_2_dict = dict(zip(ns,val_2))
val_3_dict = dict(zip(ns,val_3))
tra_1_dict = dict(zip(ns,tra_1))
tra_2_dict = dict(zip(ns,tra_2))
tra_3_dict = dict(zip(ns,tra_3))

plot_multiline('part_c_tra', [v_rate, tra_1_dict, tra_2_dict, tra_3_dict], xlabel='', ylabel='', title='', labels=['Original', 'Order1', 'Order2', 'Order3'],ylim=(0,1))
plot_multiline('part_c_val', [e_rate, val_1_dict, val_2_dict, val_3_dict], xlabel='', ylabel='', title='', labels=['Original', 'Order1', 'Order2', 'Order3'], ylim=(0,1))