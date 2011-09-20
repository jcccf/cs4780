import math, operator
from collections import defaultdict
from Loaders import *

class Node:
  def __init__(self, name, data, aa, ua, stop, mfn):
    self.data = data
    self.name = name
    self.entropy = self.__entropy(data)
    self.available_attrs = aa
    self.used_attrs = ua
    self.stop = stop
    self.children = []
    self.majority_label = self.__majority_label()
    self.max_fn_name = mfn
    if len(data) > self.stop and self.entropy > 0:
      if mfn == 'ce':
        self.__split(self.__negative_classification_error)
      elif mfn == 'ig':
        self.__split(self.__information_gain)
  
  #
  # PUBLIC
  #
  
  # Remove children from a node if all children predict the same class
  def compress(self):
    if len(self.children) > 0:
      for c in self.children:
        c.compress()
      
      have_leaves = False
      for c in self.children:
        if len(c.children) > 0:
          have_leaves = True
          break
    
      if not have_leaves:
        curr = self.children[0].majority_label
        all_same = True
        for i in range(1,len(self.children)):
          if curr != self.children[i].majority_label:
            all_same = False
            break
        if all_same:
          self.children = []

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
    #raise Exception("No Route Found!")
    return None # No examples for given attributes
  
  def predict_many(self,examples):
    return [self.predict(e) for e in examples]
    
  def count_nodes(self):
    count = 0;
    if len(self.children) > 0:
      for child in self.children:
        count += child.count_nodes()
    return 1 + count
  
  def print_tree(self, level=0):
    if self.name:
      print "-" * level + " ".join([str(x) for x in self.name])
    if len(self.children) == 0:
      if self.majority_label:
        print " " * (level+1) + self.majority_label
      else:
        print " " * (level+1) + "???"
    for child in self.children:
      child.print_tree(level=level+1)

  # returns node with least validation error
  def find_node(self,dt,val_examples,error,node):
    if len(self.children) ==0:
      return [node, error]
    my_error = ('inf')
    temp_list = None
    for child in self.children:
      [my_node, my_error] = child.find_node(dt,val_examples,error,node)
      if my_error < error:
        node = my_node
        error = my_error
      temp_list = child.children
      child.children = []
      my_error = dt.predict_error(val_examples)
      # so I don't keep popping leaf nodes
      if error > my_error and len(temp_list):
        node = child
        error = my_error
      child.children = temp_list
    return [node, error]

  #
  # PRIVATE
  #
  
  # Return the majority label/class of this node
  def __majority_label(self):
    bins = defaultdict(int)
    for d in self.data:
      bins[d.label] += 1
    if len(bins) > 0:
      return max(bins.iteritems(), key=operator.itemgetter(1))[0]
    else:
      return None # Failed to predict because there aren't any examples
  
  # Split this node, on attribute and value that maximizes max_function
  def __split(self, max_function):
    mg, mg_a, mg_v, mg_sets = float('-inf'), None, None, []
    for a in self.available_attrs:
      vals = [e.attrs[a] for e in self.data]
      for v in vals:
        if (a,v) not in self.used_attrs:
          left, right = [], []
          for d in self.data:
            if d.attrs[a] <= v:
              left.append(d)
            else:
              right.append(d)
          gain = max_function([left,right])
          if gain > mg:
            mg, mg_a, mg_v, mg_sets = gain, a, v, [left, right]

    if mg_a:
      l = Node((mg_a,'<=',mg_v), mg_sets[0], self.available_attrs, self.used_attrs +[(mg_a,mg_v)], self.stop, self.max_fn_name)
      r = Node((mg_a,'>',mg_v), mg_sets[1], self.available_attrs, self.used_attrs +[(mg_a,mg_v)], self.stop, self.max_fn_name)
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
    self.training_data = training_data
    self.node = Node(None, training_data, training_data[0].attrs.keys(), [], stopping_parameter, splitting_criterion)
    self.node.compress()
  
  # Predict the label of a single example based on the training data
  def predict(self, example):
    return self.node.predict(example)
    
  # Predict many examples at once
  def predict_many(self, examples):
    return self.node.predict_many(examples)
    
  # Calculate the test misclassification error
  def prediction_error(self, examples):
    predictions = self.predict_many(examples)
    actual = [e.label for e in examples]
    correct = 0
    for x, y in map(None, predictions, actual):
      if x == y:
        correct += 1
    pct_correct = float(correct) / len(predictions)
    pct_wrong = 1.0 - pct_correct
    return (correct, len(predictions) - correct, len(predictions), pct_correct, pct_wrong)
    
  # Calculate the test misclassification error
  def predict_error(self, examples):
    predictions = self.predict_many(examples)
    actual = [e.label for e in examples]
    correct = 0
    for x, y in map(None, predictions, actual):
      if x == y:
        correct += 1
    pct_correct = float(correct) / len(predictions)
    return 1.0 - pct_correct

  # Calculate the training misclassification error
  def training_error(self):
    return self.prediction_error(self.training_data)
    
  # Returns the # of nodes in the tree
  def count_nodes(self):
    return self.node.count_nodes()
    
  def print_tree(self):
    return self.node.print_tree()

  def find_node(self,validation_data,error):
    return self.node.find_node(self,validation_data,error,self.node)

  def prune_node(self,target):
    return self.node.prune_node(target)
    
  # Performs Reduced Error Post Pruning on the tree
  def post_prune(self,validation_data):
    error = self.predict_error(validation_data)
    [my_node, my_error] = self.find_node(validation_data,'inf')
    while my_error <= error:
      for v in my_node.children:
        my_node.children.remove(v)
      [my_node, my_error]= self.find_node(validation_data,'inf')
      print my_error
    return self

# # Toy Example
# a1 = Example('A 1:1 2:2')
# a2 = Example('B 1:2 2:2')
# a3 = Example('C 1:1 2:1')
# a4 = Example('D 1:2 2:1')
# a5 = Example('D 1:2 2:3')
# dt = DecisionTree([a1, a2, a3, a4], splitting_criterion='ce')
# # print dt.node.children[0].name
# # print dt.node.children[1].name
# # print dt.node.children[1].children[0].name
# # print dt.node.children[1].children[1].name
# # print dt.node.children[0].majority_label
# # print dt.node.children[1].majority_label
# print dt.prediction_error([a1, a2, a3, a4, a5])
