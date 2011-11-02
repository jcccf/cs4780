import commands

# Write Function To Discover Accuracy From String
def get_accuracy(stringy):
  stringy = stringy.split('\n')
  for s in stringy:
    if 'Accuracy' in s:
      nums = s.split(':')[1]
      pct, rest = nums.split('% (')
      num_correct, rest = rest.split(' correct,')
      num_incorrect, rest = rest.split(' incorrect,')
      return (float(pct), int(num_correct), int(num_incorrect))
  raise Exception('Couldn\'t find accuracy string')

def ccmp(a,b):
  if a[1] != b[1]:
    if a[1] > b[1]:
      return -1
    else:
      return 1
  else:
    if a[0] > b[0]:
      return 1
    else:
      return -1

# # PART C PART 1
# 
# cs = [10000, 0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1]
# 
# dpb = []
# for dp in range(2,6):
#   dbest = []
#   for d in range(0,10):
#     cposs = []
#     for c in cs:
#       print commands.getoutput('../bin/svm_learn -c %s -t 1 -d %d ../data/digits/digits%d.train ../data/digits/poly/digits%d_%d_%s.model' % (c,dp,d,d,dp,c))
#       cposs.append((c,commands.getoutput('../bin/svm_classify ../data/digits/digits%d.val ../data/digits/poly/digits%d_%d_%s.model ../data/digits/polyclass/digits%d_%d_%s.classified' % (d,d,dp,c,d,dp,c))))
#     cposs = [(c,get_accuracy(x)) for c,x in cposs]
#     # print cposs
#     cbest = sorted(cposs, cmp=ccmp)[0]
#     dbest.append(cbest)
#   errors = sum([a[2] for x,a in dbest])
#   dpb.append((errors, dp, dbest))
# dpb = sorted(dpb, key=lambda x:x[0])
# print dpb


# PART C PART 2

s = []
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
rdigits = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cbest = [0.0001] * 10
dp = 4
for d, c in zip(digits, cbest):
  s.append(commands.getoutput('../bin/svm_classify ../data/digits/digits.test ../data/digits/poly/digits%d_%d_%s.model ../data/digits/polybest/digits%d.classified' % (d,dp,c,d)))

errors = 0
total = 0
files = {}
for d in digits:
  files[d] = open('../data/digits/polybest/digits%d.classified' % d, 'r')
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