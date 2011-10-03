from numpy import *
from numpy.linalg import *
from scipy import sparse
from Loaders import *
from inspect import *
from ProgressBar import *
from collections import defaultdict

class FasterPerceptron:
  def __init__(self, data):
    # Load Examples in
    self.x, self.y = self.matricize(data)
    self.feature_index = {}
    
    # Initialize R
    alist = []
    for i in range(0, len(self.x)):
      alist.append(sum([x ** 2 for x in self.x[i].values()]))
    self.r2 = max(alist)
    self.r = math.sqrt(self.r2)
    print self.r
    
    # Initialize w, b, k
    self.w = defaultdict(int)
    self.b = 0
    self.k = 0 
    self.n = 1 # Learning Rate
    
    self.iterations = []

  # Convert examples into matrix form
  def matricize(self,data):
    x = []
    y = []
    
    for i in range(0, len(data)):
      x_item = {}
      for index, value in data[i].attrs.iteritems():
        x_item[int(index)] = value
      x.append(x_item)
      y.append(int(data[i].label))
    return (x,y)

  # Perform one iteration of the Perceptron algorithm
  def dot_pdt(self,a,b):
    total = 0
    for bk, bv in b.iteritems():
      total += bv * a.get(bk, 0)
    return total
    
  # DESTRUCTIVE!
  def mat_add_mul(self,a,b,c):
    for bk, bv in b.iteritems():
      a[bk] += bv * c
  
  def train(self):
    self.k = 0
    pg = ProgressBar()
    i = 0
    num_examples = len(self.x)
    for x,y in zip(self.x, self.y):
      if y * (self.dot_pdt(x,self.w) + self.b) <= 0:
        self.mat_add_mul(self.w, x, y)
        self.b += y * self.r2
        self.k += 1
      pg.update(float(i)/num_examples, 'Iterating...')
      i += 1
    pg.update(1, 'Done')
    result = (self.w, self.b, self.k)
    self.iterations.append(result)
    return result
    
  # Predict using the current vector in self.w and self.b
  def predict(self, data):
    num_incorrect, total, prediction_array = 0, len(data), []
    tx, ty = self.matricize(data)
    pg = ProgressBar()
    num_examples = len(tx)
    for i in range(0, num_examples):
      if ty[i] * (self.dot_pdt(tx[i], self.w) + self.b) <= 0:
        num_incorrect += 1
        prediction_array.append(0)
      else:
        prediction_array.append(1)
      pg.update(float(i)/num_examples, 'Predicting...')
    pg.update(1, 'Predicted')
    return (prediction_array, num_incorrect, total, float(num_incorrect)/total)

      
# d1 = Example('-1 1:0.5 8:0.6')
# d2 = Example('-1 1:0.4 9:-0.8')
# # 
# d3 = Example('-1 1:0.3 9:0.5')
# d4 = Example('1 1:0.6 9:0.7')
# # 
# # # a = sparse.lil_matrix((2,1))
# # # b = sparse.lil_matrix((2,1))
# # # c = a * b.T
# # # print c[0,0]
# # 
# p = FastPerceptron([d1,d2])
# # print "y"
# # print p.y
# # print "hi"
# # print p.x
# print p.train()
# # p.train()
# # p.train()
# # p.train()
# # print [x for a,b,x in p.iterations]
# # 
# print p.predict([d3, d4])