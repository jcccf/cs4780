import commands

# Write Function To Discover Accuracy From String
def get_error(stringy):
  stringy = stringy.split('\n')
  for s in stringy:
    if 'Zero/one-error' in s:
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

# PART 1

cs = [0.00001, 0.00005, 0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5]

cposs = []
for c in cs:
  commands.getoutput('../bin/svm_multiclass_learn -c %s ../data/digits/digits.train ../data/digits/multi/%s.model' % (c,c))
  cposs.append((c,commands.getoutput('../bin/svm_multiclass_classify ../data/digits/digits.val ../data/digits/multi/%s.model ../data/digits/multiclass/%s.classified' % (c,c))))
print cposs
cposs = [(c,get_error(x)) for c,x in cposs]

print cposs

# PART 2
c_best = 5 # I manually set this
print commands.getoutput('../bin/svm_multiclass_classify ../data/digits/digits.test ../data/digits/multi/%s.model ../data/digits/multiclass/%s.test.classified' % (c_best,c_best))