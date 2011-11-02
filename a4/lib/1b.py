import commands
import re

print '1b'
num_training = 10
cs = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1]
for i in range(num_training):
    best_accuracy = 0.0
    best_c = 0.0
    for c in cs:
        commands.getoutput('../lib/svm_learn -c %s ../data/digits/digits%d.train ../data/digits/digits%d_%s.model' %(c,i,i,c))
        print 'c=%s, output = %s' %(c,commands.getoutput('../lib/svm_classify ../data/digits/digits%d.val ../data/digits/digits%d_%s.model ../data/digits/digits%d_%s.classified' %(i,i,c,i,c)))
        s = commands.getoutput('../lib/svm_classify ../data/digits/digits%d.val ../data/digits/digits%d_%s.model ../data/digits/dump' %(i,i,c))                
        l = s.split(' ')
        m = re.search(r'\d+\D\d\d', l[16], re.I)
        accuracy = float(m.group(0))
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_c = c
    print 'best_c: %s\n\n' %best_c
    commands.getoutput('../lib/svm_classify ../data/digits/digits.test ../data/digits/digits%d_%s.model ../data/digits/digits%d.classified' %(i,best_c,i))

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
    #print poss
    best, bestval = max(poss, key=lambda x: x[1])
    if bestval < 0 or best != corr:
        pass
    else:
        num_correct += 1
    total += 1
print 'accuracy: %f' %(num_correct/total)
