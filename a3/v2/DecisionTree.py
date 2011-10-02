import math, operator
from collections import defaultdict
from Loaders import *
from types import *
from numpy import *

class perceptron:
  def __init__(self, data,v_data):
    self.data = data
    self.v_data = v_data
    self.wt_vec = {}
    self.b = 0
    self.num_attrs = self.__get_num_attrs()
    self.error = []
    
    ###### Public #########

  def get_error(self):

    R_sq = self.__find_R_sq(self.data)
    num_misclassified = 0
      
    for example in self.data:
      delta = 0
      for k,x in example.attrs.iteritems():
        delta += self.wt_vec[k] * x
      delta = int(example.label) * (delta + self.b)
      if delta <= 0:
        for k,w in example.attrs.iteritems():
          self.wt_vec[k] += int(example.label) * w
        self.b += int(example.label) * R_sq
        num_misclassified += 1

    return num_misclassified

  def find_d(self,svm,myerror):
    total = 0
    my_error = myerror.values()
    svm_error = []
    for svm_index,svm_label in svm:
      if example[svm_index].label * svm_label <= 0:
        svm_error.append(svm_index)
    d1 = set(svm_error)
    d2 = set(my_error)
    d1_error = d1 - (d1 & d2)
    d2_error = d2 - (d1 & d2)
    print 'd1: {} d2: {}'.format(d1_error,d2_error)
    

  def print_error(self):
    for e in self.error:
      print 'error: {}'.format(e)

  def get_training_error(self):

#    R_sq = self.__find_R_sq(self.v_data)
    num_misclassified = 0
    self.error = []

    for example in self.v_data:
      delta = 0
      for k,x in example.attrs.iteritems():
        delta += self.wt_vec[k] * x
      delta = int(example.label) * (delta + self.b)
      if delta <= 0:
        num_misclassified += 1
        self.error.append(k)

    return num_misclassified

    ####### Private #########

  def __normalize_wt(self):
    d = 0
    for k,v in self.wt_vec.iteritems():
      d += v*v
    d = sqrt(d)
    for k in self.wt_vec.keys():
      self.wt_vec[k] /= d

  def __get_num_attrs(self):
    set_of_keys = set(self.data[0].attrs.keys())
    for example in self.data:
      set_of_keys |= set(example.attrs.keys())

    for k in set_of_keys:
      self.wt_vec[k] = 0
    return len(self.wt_vec)

  def __find_R_sq(self,data):
    d = 0
    dlist = []
    for example in data:
      for k,x in example.attrs.iteritems():
        d += x * x
      dlist.append(d) 
      d = 0
    return max(dlist)


#a1 = Example('1 1:1 2:2')
#a2 = Example('1 1:2 2:2')
#a3 = Example('-1 1:1 2:1')
#a4 = Example('-1 1:2 2:1')
#a5 = Example('1 1:2 2:3')  
#p = perceptron([a1, a2, a3, a4, a5])
#print p.get_num_attrs()
