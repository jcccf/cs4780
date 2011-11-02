import commands
import re

print 'first part for arxiv.norm*'

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
        s.append(commands.getoutput('../lib/svm_learn -c %s ../data/arxiv/arxiv.norm%d.train ../data/arxiv/arxiv.norm%d_%s.model' % (c,d,d,c)))

    with open('../data/arxiv/arxiv%d.txt' %d, 'w') as f:
        for t in s:
            f.write(t)

for c in cs:
    s = []
    for d in range(0,nfold):
        s.append(commands.getoutput('../lib/svm_classify ../data/arxiv/arxiv.norm%d.test ../data/arxiv/arxiv.norm%d_%s.model ../data/arxiv/arxiv%d_%s.classified' % (d,d,c,d,c)))
    with open('../data/arxiv/arxiv%s_classify.txt' %c, 'w') as f:
        for t in s:
            f.write(t)

print 'now for all 4 files of a given C, find the C that on average gives the highest accuracy ...\n\n\n'
c_list = {}
for c in cs:
    accuracy = 0
    with open('../data/arxiv/arxiv%s_classify.txt' %c, 'r') as f:
        for i,l in enumerate(f):
            if (i-1)%4 == 2:
                m = re.search(r'\d+\D\d\d', l, re.I)
                accuracy += float(m.group(0))
        accuracy /= nfold        
        print 'C = %s, accuracy = %f\n\n\n' % (c,accuracy)
        c_list[float(c)] = accuracy

c_max = c_list[max(c_list.keys())]
commands.getoutput('../lib/svm_learn -c c_max arxiv.norm.train arxiv.model')
print '%s' %commands.getoutput('../lib/svm_classify arxiv.norm.test arxiv.model arxiv.classify')

nfold = 4

print 'now running arxiv.*'

s_test = []
s_train = []
for d in range(nfold):
    s_test = []
    s_train = []
    with open('../data/arxiv/arxiv.train', 'r') as f:
        for i, l in enumerate(f):
            if i%nfold == d:
                s_test.append(l)
            else:
                s_train.append(l)
    with open('../data/arxiv/arxiv%d.test' %d, 'w') as test:
        for t in s_test:
            test.write(t)
    with open('../data/arxiv/arxiv%d.train' %d, 'w') as train:
        for t in s_train:
            train.write(t)

print 'train and classify for different Cs\n\n\n'
cs = [0.001, 0.01, 0.1, 1]
s = []
for d in range(0,nfold):
    s = []
    for c in cs:
        s.append(commands.getoutput('../lib/svm_learn -c %s ../data/arxiv/arxiv%d.train ../data/arxiv/arxiv%d_%s.model' % (c,d,d,c)))

    with open('../data/arxiv/arxiv%d.txt' %d, 'w') as f:
        for t in s:
            f.write(t)

for c in cs:
    s = []
    for d in range(0,nfold):
        s.append(commands.getoutput('../lib/svm_classify ../data/arxiv/arxiv%d.test ../data/arxiv/arxiv%d_%s.model ../data/arxiv/arxiv%d_%s.classified' % (d,d,c,d,c)))
    with open('../data/arxiv/arxiv%s_classify.txt' %c, 'w') as f:
        for t in s:
            f.write(t)

print 'now for all 4 files of a given C, find the C that on average gives the highest accuracy ...\n\n\n'
list_of_c = {}
for c in cs:
    accuracy = 0
    with open('../data/arxiv/arxiv%s_classify.txt' %c, 'r') as f:
        for i,l in enumerate(f):
            if (i-1)%4 == 2:
                m = re.search(r'\d+\D\d\d', l, re.I)
                accuracy += float(m.group(0))
        accuracy /= nfold        
        print 'C = %s, accuracy = %f' % (c,accuracy)
        list_of_c[float(c)] = accuracy
        
maxc = list_of_c[max(list_of_c.keys())]

# then run svm_train and svm_classify on arxiv.train and arxiv.test with optimal C to produce arxiv_classify.txt
commands.getoutput('../lib/svm_learn -c %f ../data/arxiv/arxiv.train ../data/arxiv/arxiv.model' %maxc)
print '%s' %commands.getoutput('../lib/svm_classify ../data/arxiv/arxiv.test ../data/arxiv/arxiv.model ../data/arxiv/arxiv_classify.txt')

labels = []
false_pos = 0
false_neg = 0
with open('../data/arxiv/arxiv.test', 'r') as f:
    for i,l in enumerate(f):
        parts = l.split(' ')
        labels.append(float(parts[0]))
with open('../data/arxiv/arxiv_classify.txt', 'r') as f:
    for i,l in enumerate(f):
        parts = l.split(' ')
        if(float(parts[0]) > 0 and labels[i] < 0):
            false_pos += 1
        if(float(parts[0]) < 0 and labels[i] > 0):
            false_neg += 1
print 'false positive : %d false negative : %d' %(false_pos, false_neg)
