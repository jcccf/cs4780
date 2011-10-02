from Plotter import *

# Original from part a - note that these are reversed!
idx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
v = [621, 470, 256, 140, 162, 68, 112, 58, 16, 26, 16, 12, 2, 0, 0, 0, 0, 0, 0, 0]
v = [float(x)/1000 for x in v]
v_rate = dict(zip(idx,v))
e = [442, 258, 227, 222, 233, 236, 220, 219, 225, 222, 228, 219, 227, 227, 227, 227, 227, 227, 227, 227]
e = [float(x)/1000 for x in e]
e_rate = dict(zip(idx,e))

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