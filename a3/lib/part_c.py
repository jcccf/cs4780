from FastPerceptron import *
from Loaders import *
from optparse import OptionParser

vali = load_data('../data/polarity.validation')

files = ['../data/polarity.train', '../data/polarity-reorder-1.train', '../data/polarity-reorder-2.train', '../data/polarity-reorder-3.train']
fnames = ['orig', 're1', 're2', 're3']

# Options
parser = OptionParser()
parser.add_option("-r", "--train", type="int", dest="train", default=1, help="Training Data File #")
#parser.add_option("-t", "--name", type="int", dest="name", default=1, help="Name #")
(options, args) = parser.parse_args()


# for af, an in zip(files, fnames):
def do_it(af, an):
  print "Loading for %s" % an
  data = load_data(af)
  p = FastPerceptron(data)
  
  zall = []
  for i in range(0,20):
    print "Iteration %d" % i
    p.train()
    print "Predicting..."
    ps,x,y,z = p.predict(vali)
    with open('../data/partc/tron_%s_%d.res' % (an, i), 'w') as f:
      for q in ps:
        f.write(str(q)+'\n')
    with open('../data/partc/tron_%s_%d.txt' % (an, i), 'w') as f:
      f.write(str(x)+'\n')
      f.write(str(y)+'\n')
      f.write(str(z)+'\n')
    zall.append(z)
    
  with open('../data/partc/tron_%s_all2.txt' % an, 'w') as f:
    for z in zall:
      f.write(str(z)+'\n')
  
  with open('../data/tron_%s_all.txt' % an, 'w') as f:
    for a,b,x in p.iterations:
      f.write(str(x)+'\n')
  
  print [x for a,b,x in p.iterations]
  
do_it(files[options.train], fnames[options.train])