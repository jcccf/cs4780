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

# Splits the list l into npieces pieces
def parts(l, npieces):
  parts = []
  size = len(l)/npieces
  for i in range(0, npieces-1):
    parts.append(l[i*size:(i+1)*size])
  parts.append(l[size*(npieces-1):])
  return parts

avg_error = []
tsets = parts(training_set, 10)
pg, prog = ProgressBar(), 1.0
for s_para in s_paras:
  op = prog/s_len
  ip = 1.0
  test_error = []
  for p in tsets:
    train = []
    for q in tsets:
      if p != q:
        train += q
    test = p
    dt = DecisionTree(train, stopping_parameter=s_para)
    test_error.append(dt.prediction_error(test)[1])
    pg.update(-(1-ip/10)/s_len+op, "Stopping Para %d" % s_para)
    ip += 1
  #print test_error
  avg_error.append((s_para, float(sum(test_error))/len(test_error)))
  prog += 1
  
top = sorted(avg_error, key = lambda (_,e) : e)[0]
print avg_error
print "Stopping Parameter and Error: %d, %f" % (top[0], top[1])

# Build decision tree with "best" parameter trained on original
print "Using these values to get training and test error"
dt = DecisionTree(training_set, stopping_parameter=top[0])
print dt.training_error()
print dt.prediction_error(test_set)
