import commands

## PART B SVMLIGHT

# cs = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1]
# 
# for d in range(0,10):
#   s = []
#   for c in cs:
#     s.append(commands.getoutput('../bin/svm_learn -c %s ../data/digits/digits%d.train ../data/digits/models/digits%d_%s.model' % (c,d,d,c)))
#   
#   with open('../data/digits/models/digits%d.txt' % d, 'w') as f:
#     for t in s:
#       f.write(t+'\n\n\n')
# 
# for d in range(0,10):
#   s = []
#   for c in cs:
#     s.append(commands.getoutput('../bin/svm_classify ../data/digits/digits%d.val ../data/digits/models/digits%d_%s.model ../data/digits/class/digits%d_%s.classified' % (d,d,c,d,c)))
#   
#   with open('../data/digits/class/digits%d_classify.txt' % d, 'w') as f:
#     for t in s:
#       f.write(t+'\n\n\n')

# PART B PART 2

s = []
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
rdigits = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#cbest = [0.1, 0.01, 0.01, 0.0001, 0.01, 0.1, 0.01, 0.1, 0.1, 0.001]
cbest = [0.0001, 0.005, 0.0001, 0.0001, 0.01, 0.0005, 0.0005, 0.0005, 0.1, 0.001]
for d, c in zip(digits, cbest):
  s.append(commands.getoutput('../bin/svm_classify ../data/digits/digits.test ../data/digits/models/digits%d_%s.model ../data/digits/best/digits%d.classified' % (d,c,d)))

errors = 0
total = 0
files = {}
for d in digits:
  files[d] = open('../data/digits/best/digits%d.classified' % d, 'r')
testfile = open('../data/digits/digits.test', 'r')
for l in testfile:
  corr = int(l.split(' ', 2)[0])
  poss = []
  for d,d2 in zip(digits,rdigits):
    poss.append((d2,float(files[d].readline())))
  print poss
  best, bestval = max(poss, key=lambda x: x[1])
  if bestval < 0 or best != corr:
    print bestval, best, corr
    errors += 1
  total += 1
print errors, total