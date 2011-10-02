import commands

## PART B SVMLIGHT

cs = [0.25, 0.5, 1, 2, 4, 8, 16, 32, 64]

s = []
for c in cs:
  s.append(commands.getoutput('svm_learn -c %s ../data/polarity.train ../data/polarity_%s.model' % (c,c)))
  
with open('../data/polarity_results.txt', 'w') as f:
  for t in s:
    f.write(t+'\n\n\n')

s = []
for c in cs:
  s.append(commands.getoutput('svm_classify ../data/polarity.validation ../data/polarity_%s.model ../data/polarity_%s.result' % (c,c)))
  
with open('../data/polarity_results2.txt', 'w') as f:
  for t in s:
    f.write(t+'\n\n\n')
  

## PART C SVMLIGHT
  
s = []
trains = ['polarity.train', 'polarity-reorder-1.train', 'polarity-reorder-2.train', 'polarity-reorder-3.train']
for t in trains:
  s.append(commands.getoutput('svm_learn -c 8 ../data/%s ../data/%s_8.model' % (t,t)))
  
with open('../data/polarity_results3.txt', 'w') as f:
  for t in s:
    f.write(t+'\n\n\n')
  
s = []
for t in trains:
  s.append(commands.getoutput('svm_classify ../data/polarity.validation ../data/%s_8.model ../data/%s_8.result' % (t,t)))
  
with open('../data/polarity_results4.txt', 'w') as f:
  for t in s:
    f.write(t+'\n\n\n')