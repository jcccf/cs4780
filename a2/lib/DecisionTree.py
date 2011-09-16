import math

('lessthan',a, 30)

class Node:
  def __init__(self, name, data, available_attributes):
    self.children = []
    self.data = data
    self.name = name
    self.entropy = self.entropy(data)
    self.available_attributes = []
    
    if 
    
  def split(self):
    mg, mg_a, mg_v, mg_sets = 0, None, vals[0], []
    for a in self.available_attributes:
      vals = [e.features[a] for e in data]
      
      for v in vals:
        left, right = [], []
        for d in self.data:
          if d.features[a] <= v:
            left.append(d)
          else:
            right.append(d)
        gain = info_gain([left,right])
        if gain > max_gain:
          mg, mg_a, mg_v, mg_sets = gain, a, v, [left, right]
      
      # SPLIT ON THIS
      new_attributes = list(self.available_attributes)
      new_attributes.remove(mg_a)
      left_node = Node((mg_a,'leq',mg_v), mg_sets[0], new_attributes)
      right_node = Node((mg_a,'gt',mg_v), mg_sets[1], new_attributes)


  def info_gain(self,sets):
    num_elts = 0
    for s in sets:
      num_elts += len(s)
      
    gain = self.entropy
    for s in sets:
      gain -= float(len(s)) / num_elts * self.entropy(data)
      
    return gain
  
  def entropy(self,data):
    num_elts = len(data)
    bins = {}
    
    for d in data:
      if bins[d.label]:
        bins[d.label] += 1
      else:
        bins[d.label] = 1
        
    entropy = 0
    for v in bins.values():
      fraction = v/num_elts
      entropy += -fraction * math.log(fraction,2)
  
    return entropy

class DecisionTree:
  
  def __init__(self, training):