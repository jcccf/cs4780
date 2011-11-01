from Bayes import *
import commands
import re

print '3b'
bc = Bayes()
bc.train('../data/arxiv/arxiv.train')
bc.predict('../data/arxiv/arxiv.test', 0, 1, 1, 0)

print '3c'

c = Bayes()
c.train('../data/arxiv/arxiv.train')
c.predict('../data/arxiv/arxiv.test', 0, 1, 10, 0)

print '3d'
nfold = 4
s_test = []
s_train = []
for d in range(nfold):
  s_test = []
  s_train = []
  with open('../data/arxiv/arxiv.norm.train', 'r') as f:
    for i, l in enumerate(f):
      if i%nfold == d:
        s_test.append(l)
      else:
        s_train.append(l)
  with open('../data/arxiv/arxiv.norm%d.test' %d, 'w') as test:
    for t in s_test:
      test.write(t)
  with open('../data/arxiv/arxiv.norm%d.train' %d, 'w') as train:
    for t in s_train:
      train.write(t)

print 'train and classify for different Cs\n\n\n'
cs = [0.001, 0.01, 0.1, 1]
s = []
for d in range(0,nfold):
    s = []
    for c in cs:
        s.append(commands.getoutput('../lib/svm_learn -j 10 -c %s ../data/arxiv/arxiv.norm%d.train ../data/arxiv/arxiv.norm%d_%s.model' % (c,d,d,c)))

    with open('../data/arxiv/arxiv%d.txt' %d, 'w') as f:
        for t in s:
            f.write(t)

for c in cs:
    s = []
    for d in range(0,nfold):
        s.append(commands.getoutput('../lib/svm_classify ../data/arxiv/arxiv.norm%d.test ../data/arxiv/arxiv.norm%d_%s.model ../data/arxiv/arxivs%d_%s.classified' % (d,d,c,d,c)))
    with open('../data/arxiv/arxivs%s_classify.txt' %c, 'w') as f:
        for t in s:
            f.write(t)

false_pos = 0
false_neg = 0
labels = []
for c in cs:
  false_pos = 0
  false_neg = 0
  for d in range(nfold):
    labels = []
    with open('../data/arxiv/arxiv.norm%d.test' %d, 'r') as f:
      for i,l in enumerate(f):
        parts = l.split(' ')
        labels.append(float(parts[0]))
    with open('../data/arxiv/arxivs%d_%s.classified' %(d,c), 'r') as f:
      for i,l in enumerate(f):
        parts = l.split(' ')
        if float(parts[0]) > 0 and labels[i] < 0:
          false_pos += 1
        if float(parts[0]) < 0 and labels[i] > 0:
          false_neg += 1
  print 'c = %s false positive = %d false negative = %d' %(c,false_pos,false_neg)

cguess = {}
print 'now for all 4 files of a given C, find the C that on average gives the highest accuracy ...\n\n\n'
for c in cs:
    accuracy = 0
    with open('../data/arxiv/arxivs%s_classify.txt' %c, 'r') as f:
        for i,l in enumerate(f):
            if (i-1)%4 == 2:
                m = re.search(r'\d+\D\d\d', l, re.I)
                accuracy += float(m.group(0))
        accuracy /= nfold        
        print 'C = %s, accuracy = %f' % (c,accuracy)
        cguess[float(c)] = accuracy

cmax = cguess[max(cguess.keys())]

labels = []
commands.getoutput('../lib/svm_learn -j 10 -c %f ../data/arxiv/arxiv.norm.train ../data/arxiv/arxiv.norm.model' %cmax)
print '%s' %commands.getoutput('../lib/svm_classify ../data/arxiv/arxiv.norm.test ../data/arxiv/arxiv.norm.model ../data/arxiv/arxiv.norm.classified')

false_pos = 0
false_neg = 0
labels = []
with open('../data/arxiv/arxiv.norm.test', 'r') as f:
    for i,l in enumerate(f):
        parts = l.split(' ')
        labels.append(float(parts[0]))
with open('../data/arxiv/arxiv.norm.classified', 'r') as f:
    for i,l in enumerate(f):
        parts = l.split(' ')
        if(float(parts[0]) > 0 and labels[i] < 0):
          false_pos += 1
        if(float(parts[0]) < 0 and labels[i] > 0):
          false_neg += 1
print 'false positive : %d , false negative : %d' %(false_pos, false_neg)
