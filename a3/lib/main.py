from Perceptron import *
from Loaders import *

data = load_data('../data/polarity.train')
vali = load_data('../data/polarity.validation')

p = Perceptron(data)

for i in range(0,20):
  print "Iteration %d" % i
  p.train()
  print "Predicting..."
  p,x,y,z = p.predict(vali)
  with open('../data/tron_%d.res' % i, 'w') as f:
    for q in p:
      f.write(str(q)+'\n')
  with open('../data/tron_%d.txt' % i, 'w') as f:
    f.write(str(x)+'\n')
    f.write(str(y)+'\n')
    f.write(str(z)+'\n')

with open('../data/tron_all.txt', 'w') as f:
  for a,b,x in p.iterations:
    f.write(x+'\n')

print [x for a,b,x in p.iterations]