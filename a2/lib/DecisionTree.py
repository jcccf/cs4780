import math, operator
from collections import defaultdict
from Loaders import *

class Node:
  def __init__(self, name, data, aa, stop, mfn):
    self.data = data
    self.name = name
    self.entropy = self.__entropy(data)
    self.available_attrs = aa
    self.stop = stop
    self.children = []
    self.majority_label = self.__majority_label()
    self.max_fn_name = mfn
    if len(data) > self.stop:
      if mfn == 'ce':
        self.__split(self.__negative_classification_error)
      elif mfn == 'ig':
        self.__split(self.__information_gain)
  
  #
  # PUBLIC
  #
  
  # Predict the label of the example
  def predict(self,example):
    if len(self.children) == 0:
      return self.majority_label
    else:
      for child in self.children:
        a, op, v = child.name
        if a not in example.attrs:
          raise Exception("Attribute access error")
        if eval('example.attrs[a] %s v' % op):
          return child.predict(example)
    raise Exception("No Route Found!")
  
  def predict_many(self,examples):
    return [self.predict(e) for e in examples]
  
  #
  # PRIVATE
  #
  
  # Return the majority label/class of this node
  def __majority_label(self):
    bins = defaultdict(int)
    for d in self.data:
      bins[d.label] += 1
    return max(bins.iteritems(), key=operator.itemgetter(1))[0]
  
  # Split this node, on attribute and value that maximizes max_function
  def __split(self, max_function):
    mg, mg_a, mg_v, mg_sets = float('-inf'), None, None, []
    for a in self.available_attrs:
      vals = [e.attrs[a] for e in self.data]
      for v in vals:
        left, right = [], []
        for d in self.data:
          if d.attrs[a] <= v:
            left.append(d)
          else:
            right.append(d)
        gain = max_function([left,right])
        if gain > mg:
          mg, mg_a, mg_v, mg_sets = gain, a, v, [left, right]

    new_attr = list(self.available_attrs)
    new_attr.remove(mg_a)
    l = Node((mg_a,'<=',mg_v), mg_sets[0], new_attr, self.stop, self.max_fn_name)
    r = Node((mg_a,'>',mg_v), mg_sets[1], new_attr, self.stop, self.max_fn_name)
    self.children = [l, r]
  
  # Calculate the entropy of data
  def __entropy(self,data):
    num_elts = len(data)
    bins = defaultdict(int)
    for d in data:
      bins[d.label] += 1
    ent = 0
    for v in bins.values():
      fraction = float(v)/num_elts
      ent += -fraction * math.log(fraction,2)
    return ent

  # Calculates information gain of the candidate sets
  def __information_gain(self,sets):
    num_elts = 0
    for s in sets:
      num_elts += len(s)
    gain = self.entropy
    for s in sets:
      f = float(len(s))
      gain -= (f / num_elts * self.__entropy(s))
    return gain
    
  # Calculates the classification error of the candidate sets
  def __negative_classification_error(self,sets):
    num_errors = 0
    for s in sets:
      bins = defaultdict(int)
      for d in s:
        bins[d.label] += 1
      if len(s) > 0:
        majority_num = max(bins.iteritems(), key=operator.itemgetter(1))[1]
        num_errors += len(s) - majority_num
    # Return negative because we want to maximize
    return -num_errors 

class DecisionTree:
  def __init__(self, training_data, stopping_parameter=1, splitting_criterion='ig'):
    self.node = Node(None, training_data, training_data[0].attrs.keys(), stopping_parameter, splitting_criterion)
  
  # Predict the label of a single example based on the training data
  def predict(self, example):
    return self.node.predict(example)
    
  # Predict many examples at once
  def predict_many(self, examples):
    return self.node.predict_many(examples)
    
  # Calculate the misclassification error for examples
  def prediction_error(self, examples):
    predictions = self.predict_many(examples)
    actual = [e.label for e in examples]
    correct = 0
    for x, y in map(None, predictions, actual):
      if x == y:
        correct += 1
    pct_correct = float(correct) / len(predictions)
    return (correct, len(predictions), pct_correct)
    
  # Returns the # of nodes in the tree
  def count_nodes(self):
    # TO BE IMPLEMENTED
    return None
    
  # Performs Reduced Error Post Pruning on the tree
  def post_prune(self):
    # TO BE IMPLEMENTED
    return None

# Toy Example
a1 = Example('A 1:1 2:2')
a2 = Example('B 1:2 2:2')
a3 = Example('C 1:1 2:1')
a4 = Example('D 1:2 2:1')
a5 = Example('D 1:2 2:3')
dt = DecisionTree([a1, a2, a3, a4])
# print dt.node.children[0].name
# print dt.node.children[1].name
# print dt.node.children[1].children[0].name
# print dt.node.children[1].children[1].name
# print dt.node.children[0].majority_label
# print dt.node.children[1].majority_label
print dt.prediction_error([a1, a2, a3, a4, a5])