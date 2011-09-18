from Loaders import *
from DecisionTree import *
from Plotter import *
from ProgressBar import *

training_set = load_data('bcan.train')
test_set = load_data('bcan.test')
validation_set = load_data('bcan.validate')
s_paras = [1, 5, 9, 17, 25, 37, 43, 49]
#s_paras = [49]
s_len = float(len(s_paras))

train_errors, test_errors, prog = {}, {}, 1
table = {}
pg = ProgressBar()
for s_para in s_paras:
  dt = DecisionTree(training_set, stopping_parameter=s_para)
  #dt.print_tree()
  nodes = dt.count_nodes()
  table[nodes] = (dt.prediction_error(validation_set), dt.prediction_error(test_set))
  test_errors[nodes] = dt.prediction_error(test_set)[2]
  train_errors[nodes] = dt.training_error()[2]
  pg.update(prog/s_len, 'Info Gain')
  prog += 1
  
plot_multiline('part_a', [train_errors,test_errors], labels=['Training','Testing'])
print table

train_errors, test_errors, prog = {}, {}, 1
table = {}
pg = ProgressBar()
for s_para in s_paras:
  dt = DecisionTree(training_set, stopping_parameter=s_para, splitting_criterion='ce')
  #dt.print_tree()
  nodes = dt.count_nodes()
  table[nodes] = (dt.prediction_error(validation_set), dt.prediction_error(test_set))
  test_errors[nodes] = dt.prediction_error(test_set)[2]
  train_errors[nodes] = dt.training_error()[2]
  pg.update(prog/s_len, 'Classification Error')
  prog += 1

plot_multiline('part_b', [train_errors,test_errors], labels=['Training','Testing'])
print table