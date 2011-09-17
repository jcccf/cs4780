class Example:
  def __init__(self, line='0'):
    parts = line.split(' ')
    self.label = parts[0]
    self.attrs = {}
    for i in range(1,len(parts)):
      if ':' in parts[i]:
        feature = parts[i].split(':')
        if len(feature) is 2:
          self.attrs[int(feature[0])] = float(feature[1])
        else:
          print "Error in length of feature for %s" % self.label

# Load data from a file and return an array of Examples
def load_data(filename):
  data = []
  with open("../data/%s" % filename) as f:
  	for l in f:
  		data.append(Example(l))
  return data