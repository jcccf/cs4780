import commands
import re

print '1c'
cs = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1]
num_digits = 10
d_range = [2,3,4,5]

best_sum = 0.0
best_d = 0
list_of_cs = []
for d in d_range:
    sum_accuracy = 0.0
    for i in range(num_digits):
        best_accuracy = 0.0
        best_c = 0.0
        for c in cs:
            commands.getoutput('../lib/svm_learn -c %s -t 1 -d %d ../data/digits/digits%d.train ../data/digits/digits%d_%s.model' %(c,d,i,i,c))
            s = commands.getoutput('../lib/svm_classify ../data/digits/digits%d.val ../data/digits/digits%d_%s.model dump' %(i,i,c))
            l = s.split(' ')
            m = re.search(r'\d+\D\d\d', l[16], re.I)
            accuracy = float(m.group(0))
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_c = c
        
        s = commands.getoutput('../lib/svm_classify ../data/digits/digits%d.val ../data/digits/digits%d_%s.model dump' %(i,i,best_c))
        list_of_cs.append(best_c)
        print '%s' %s
        l = s.split(' ')
        m = re.search(r'\d+\D\d\d', l[16], re.I)
        sum_accuracy += float(m.group(0))
    if best_sum < sum_accuracy:
        best_sum = sum_accuracy
        best_d = d

print 'best_d: %d' %best_d

num_correct = 0
labels = []
files = {}
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
rdigits = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
for d in digits:
    files[d] = open('../data/digits/digits%d.classified' %d, 'r')
testfile = open('../data/digits/digits.test', 'r')
for l in testfile:
    corr = int(l.split(' ', 2)[0])
    poss = []
    for d,d2 in zip(digits,rdigits):
        poss.append((d2,float(files[d].readline())))
    best, bestval = max(poss, key=lambda x: x[1])
    if bestval < 0 or best != corr:
        pass
    else:
        num_correct += 1
    total += 1
print 'accuracy: %f' %(num_correct/total)
