import math, operator
from collections import defaultdict

class Bayes:
    def __init__(self):
        self.nplus = 0 #number of +/- examples
        self.nminus = 0
        self.prob_y_plus = 0 # probability of y= +/- 1
        self.prob_y_minus = 0
        self.v = 0 #total number of distinct words in document
        self.lplus = 0 # total number of distinct words labeled +/-1
        self.lminus = 0
        self.wplus = defaultdict(int) # word counts for each word in examples labeled +/- 1
        self.wminus = defaultdict(int)

    def train(self, filename):    
        with open('../data/%s' % filename, 'r') as f:
            for l in f:
                parts = l.split(' ')
                if int(parts[0]) > 0:
                    self.nplus += 1
                    for w in range(1, len(parts)):
                        if ':' in parts[w]:
                            word = parts[w].split(':')
                            if int(word[0]) not in self.wminus and int(word[0]) not in self.wplus:
                                self.v += 1
                            self.wplus[int(word[0])] += int(word[1])
                            self.lplus += int(word[1])
                        
                else:
                    self.nminus += 1
                    for w in range(1, len(parts)):
                        if ':' in parts[w]:
                            word = parts[w].split(':')
                            if int(word[0]) not in self.wminus and int(word[0]) not in self.wplus:
                                self.v += 1
                            self.wminus[int(word[0])] += int(word[1])
                            self.lminus += int(word[1])
        self.prob_y_plus = math.log(float(self.nplus)/float(self.nplus + self.nminus))
        self.prob_y_minus = math.log(float(self.nminus)/float(self.nplus + self.nminus))
        print 'v: %d, prob_y_plus : %f, prob_y_minus: %f, lplus: %d, lminus: %d' %(self.v,self.prob_y_plus,self.prob_y_minus,self.lplus,self.lminus)

    def predict(self, filename, c00, c01, c10, c11):
        num_correct = 0
        decide_plus = 0
        decide_minus = 0
        decision = 0
        false_pos = 0
        false_neg = 0
        label = 0
        with open('../data/%s' % filename, 'r') as f:
            for i, l in enumerate(f):
                parts = l.split(' ')
                label = int(parts[0])
                decide_plus = self.prob_y_plus
                decide_minus = self.prob_y_minus
                for w in range(1, len(parts)):
                    if ':' in parts[w]:
                        word = parts[w].split(':')
                        if int(word[0]) in self.wplus:
                            decide_plus += math.log(float(self.wplus[int(word[0])]+1.0)/float(self.lplus + self.v))
                        else:
                            decide_plus += math.log(1.0/float(self.lplus + self.v))
                        if int(word[0]) in self.wminus:
                            decide_minus += math.log(float(self.wminus[int(word[0])]+1.0)/float(self.lminus + self.v))
                        else:
                            decide_minus += math.log(1.0/float(self.lminus + self.v))
                if c00 == 0 and c11 == 0 and c01 == 1 and c10 == 1:
                    if decide_plus > decide_minus:
                        decision = 1
                    elif decide_plus < decide_minus:
                        decision = -1
                    else:
                        if self.nplus > self.nminus:
                            decision = 1
                        elif self.nplus < self.nminus:
                            decision = -1
                        else:
                            print "error! tie in prediction"
                else:
                    decide_plus += math.log(c10-c11)
                    decide_minus += math.log(c01-c00)
                    if decide_plus >= decide_minus:
                        decision = 1
                    else:
                        decision = -1
                if decision == label:
                    num_correct +=1
                elif (decision == 1 and label == -1):
                    false_pos += 1
                elif (decision == -1 and label == 1):
                    false_neg += 1
        print "finished predicting ... accuracy : %f, false positives: %d, false negatives: %d" %(float(num_correct)/float(i+1),false_pos,false_neg)


        
