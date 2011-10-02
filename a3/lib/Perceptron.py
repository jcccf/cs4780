from numpy import *
from numpy.linalg import *
from scipy import sparse
from Loaders import *
from inspect import *
from ProgressBar import *

class Perceptron:
  def __init__(self, data, num_features=30000):
    raise Exception("Need to Fix R Here!!!")
    # Load Examples in
    self.num_features = num_features
    self.x, self.y = self.matricize(data)
    
    # Initialize R
    xa = self.x.toarray()
    f_max, f_min = xa.max(0), xa.min(0) # get max/min val of each feature
    f_min = -f_min # so that most negative numbers become most positive
    self.r = max(f_max.max(), f_min.max()) # set the max radius
    self.r2 = self.r ** 2
    #print self.r
    
    # Initialize w, b, k
    self.w = sparse.lil_matrix((1,num_features))
    self.b = 0
    self.k = 0 
    self.n = 1 # Learning Rate
    
    self.iterations = []

  # Convert examples into matrix form
  def matricize(self,data):
    x = sparse.lil_matrix((len(data),self.num_features))
    y = sparse.lil_matrix((len(data),1))
    for i in range(0, len(data)):
      for index, value in data[i].attrs.iteritems():
        x[i,int(index)] = float(value)
      y[i,0] = int(data[i].label)
    return (x,y)

  # Perform one iteration of the Perceptron algorithm
  def train(self):
    self.k = 0
    pg = ProgressBar()
    num_examples = self.x.shape[0]
    for i in range(0, num_examples):
      if self.y[i,0] * ((self.x[i,:] * self.w.T)[0,0] + self.b) <= 0:
        self.w += self.n * self.y[i,0] * self.x[i,:]
        self.b += self.n * self.y[i,0] * self.r2
        self.k += 1
      #print "hi"
      pg.update(float(i)/num_examples, 'Iterating...')
    pg.update(1, 'Done')
    result = (self.w, self.b, self.k)
    self.iterations.append(result)
    return result
    
  # Predict using the current vector in self.w and self.b
  def predict(self, data):
    num_incorrect, total, prediction_array = 0, len(data), []
    tx, ty = self.matricize(data)
    pg = ProgressBar()
    num_examples = tx.shape[0]
    for i in range(0, num_examples):
      if ty[i,0] * ((tx[i,:] * self.w.T)[0,0] + self.b) <= 0:
        num_incorrect += 1
        prediction_array.append(0)
      else:
        prediction_array.append(1)
      pg.update(float(i)/num_examples, 'Predicting...')
    pg.update(1, 'Predicted')
    return (prediction_array, num_incorrect, total, float(num_incorrect)/total)

      
# d1 = Example('-1 1:0.5 8:0.6')
# d2 = Example('-1 1:0.4 9:0.7')
# 
# d3 = Example('-1 1:0.3 9:0.5')
# d4 = Example('1 1:0.6 9:0.7')
# 
# # a = sparse.lil_matrix((2,1))
# # b = sparse.lil_matrix((2,1))
# # c = a * b.T
# # print c[0,0]
# 
# p = Perceptron([d1,d2])
# # print "y"
# # print p.y
# # print "hi"
# # print p.x
# p.train()
# p.train()
# p.train()
# p.train()
# print [x for a,b,x in p.iterations]
# 
# print p.predict([d3, d4])