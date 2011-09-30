from Perceptron import *
from Loaders import *


vali = load_data('../data/polarity.validation')

files = ['../data/polarity.train', '../data/polarity-reorder-1.train', '../data/polarity-reorder-2.train', '../data/polarity-reorder-3.train']
fnames = ['orig', 're1', 're2', 're3']
for af, an in zip(files, fnames):
  print "Loading for %s" % an
  data = load_data(af)
  p = Perceptron(data)
  
  zall = []
  for i in range(0,20):
    print "Iteration %d" % i
    p.train()
    print "Predicting..."
    p,x,y,z = p.predict(vali)
    with open('../data/partc/tron_%s_%d.res' % (an, i), 'w') as f:
      for q in p:
        f.write(q+'\n')
    with open('../data/partc/tron_%s_%d.txt' % (an, i), 'w') as f:
      f.write(x+'\n')
      f.write(y+'\n')
      f.write(z+'\n')
    zall.append(z)
    
  with open('../data/partc/tron_%s_all2.txt' % an, 'w') as f:
    for z in zall:
      f.write(z+'\n')
  
  with open('../data/tron_%s_all.txt' % an, 'w') as f:
    for a,b,x in p.iterations:
      f.write(x+'\n')
  
  print [x for a,b,x in p.iterations]