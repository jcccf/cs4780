from Perceptron import *
from FastPerceptron import *
from FasterPerceptron import *
from Loaders import *

data = load_data('../data/polarity.train')
vali = load_data('../data/polarity.validation')

p = FasterPerceptron(data)

for i in range(0,20):
  print "Iteration %d" % i
  p.train()
  print "Predicting..."
  ps,x,y,z = p.predict(vali)
  with open('../data/ftron_%d.res' % i, 'w') as f:
    for q in ps:
      f.write(str(q)+'\n')
  with open('../data/ftron_%d.txt' % i, 'w') as f:
    f.write(str(x)+'\n')
    f.write(str(y)+'\n')
    f.write(str(z)+'\n')

with open('../data/ftron_all.txt', 'w') as f:
  for a,b,x in p.iterations:
    f.write(str(x)+'\n')

print [x for a,b,x in p.iterations]