import commands

def classify(test_file, model_file, classified_file):
  return commands.getoutput('../bin/svm_classify %s %s %s' % (test_file, model_file, classified_file))
  
def learn(train_file, model_file, c=None, j=None):
  c_string = ""
  if c:
    c_string = "-c %s " % c
  j_string = ""
  if j:
    j_string = "-j %s " % j
  # print 'svm_learn %s%s%s %s' % (c_string, j_string, train_file, model_file)
  return commands.getoutput('../bin/svm_learn %s%s%s %s' % (c_string, j_string, train_file, model_file))
  
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
  
def split_for_validation(example_file, num=4):
  with open(example_file, 'r') as f:
    lines = f.readlines()
  size = len(lines) / num
  for i in range(0, num):
    with open("%s.%d.tr" % (example_file, i), 'w') as f:
      with open("%s.%d.va" % (example_file, i), 'w') as f2:
        for j in range(0, len(lines)):
          if j % num != i:
            f.write(lines[j])
          else:
            f2.write(lines[j])

def get_cross_val_accuracy(train_file, num=4, c=None, j=None):
  split_for_validation(train_file, num)
  accuracies = []
  for i in range(0, num):
    learn("%s.%d.tr" % (train_file, i), "%s.%d.tr.mod" % (train_file, i), c, j)
    accuracies.append(get_accuracy(classify("%s.%d.va" % (train_file, i), "%s.%d.tr.mod" % (train_file, i), "%s.%d.tr.cls" % (train_file, i))))
    print get_false_posneg("%s.%d.va" % (train_file, i), "%s.%d.tr.cls" % (train_file, i))
  cc, ic = 0, 0
  for _, c, i in accuracies:
    cc += c
    ic += i
  return (float(cc)/(cc+ic), cc, ic)
  
def get_false_posneg(test_file, classified_file):
  false_pos, false_neg = 0, 0
  f, cf = open(test_file, 'r'), open(classified_file, 'r')
  for l in f:
    f_val = int(l.replace('\n','').split(' ', 2)[0])
    cf_val = float(cf.readline().replace('\n',''))
    if f_val * cf_val < 0:
      if cf_val < 0:
        false_neg += 1
      else:
        false_pos += 1
  f.close()
  cf.close()
  return (false_pos, false_neg)