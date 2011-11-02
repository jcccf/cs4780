from Loaders import *
from collections import defaultdict
import math

class BayesClassifier:
  
  def __init__(self, data):
    self.data = data
    
    # Determine the dictionary size
    max_attrs = []
    for e in data:
      max_attrs.append(max(e.attrs))
    self.dict_size = int(max(max_attrs))
    
    # Compute global word frequency and number of documents in each class
    classes = defaultdict(int)
    attrs = defaultdict(int)
    for e in data:
      classes[e.label] += 1
      for a, v in e.attrs.iteritems():
        attrs[(a,e.label)] += v

    # Pre-compute ln(Pr(Y=y))
    self.lnPrY = {}
    for l,n in classes.iteritems():
      self.lnPrY[l] = math.log(float(n)/len(data))
    self.numY = classes
    
    # Get # of all words in documents with class y
    self.attr_total = defaultdict(int) 
    for ay, v in attrs.iteritems():
      self.attr_total[ay[1]] += v
    
    # Pre-compute ln(Pr(W=w|Y=y))
    self.lnPrWgY = {}
    for ay, v in attrs.iteritems():
      self.lnPrWgY[ay] = math.log(float(v+1) / (self.attr_total[ay[1]] + self.dict_size))
    
  # Use this to access Pr(W=w|Y=y) so that unset values are also returned properly
  def __WgY__(self, w, y):
    if not (w,y) in self.lnPrWgY:
      self.lnPrWgY[(w,y)] = math.log(float(1) / (self.attr_total[y] + self.dict_size))
    return self.lnPrWgY[(w,y)]
    
  def predict(self, example):
    sums = []
    for y, lnpry in self.lnPrY.iteritems():
      curr = lnpry
      for a, v in example.attrs.iteritems():
        for i in range(0,int(v)): #for each occurence of some word, add ln Pr(W=w|Y=y)
          curr += self.__WgY__(a,y)
          # break # HACKY?
      sums.append((y,curr))
    # print sums
    if sums[0][1] == sums[1][1]:
      return '1' # Hardcoded
    else:
      return max(sums, key=lambda x: x[1])[0]

  # This function only works if there are 2 classes!!!
  # The rest work even if there are >2 classes
  def cost_sensitive_predict(self, example):
    costs_y = {'1': math.log(10), '-1': math.log(1)} # this is c_10 and c_01
    sums = []
    for y, lnpry in self.lnPrY.iteritems():
      curr = lnpry
      for a, v in example.attrs.iteritems():
        for i in range(0,int(v)):
          curr += self.__WgY__(a,y)
          # break
      sums.append((y, costs_y[y] + curr)) # add because these are logs
    return max(sums, key=lambda x: x[1])[0]
    
  # This function only works if there are 2 classes!!!
  # The rest work even if there are >2 classes
  def predict_all(self, examples, cost_sensitive=False):
    num_correct, false_pos, false_neg = 0, 0, 0
    num_pos, num_neg = 0, 0
    for example in examples:
      if cost_sensitive:
        predicted = self.cost_sensitive_predict(example)
      else:
        predicted = self.predict(example)
      if predicted == example.label:
        if predicted == '1':
          num_pos += 1
        else:
          num_neg += 1
        num_correct += 1
      elif predicted == '1':
        false_pos += 1
      elif predicted == '-1':
        false_neg += 1
    return (num_correct, false_pos, false_neg)


data = load_data('../data/arxiv/arxiv.train')
bc = BayesClassifier(data)
exs = [Example('-1 1:3 2:1 3:2 4:8 5:2 6:2 7:2 8:1 9:2 10:1 11:1 12:6 13:3 14:1 15:1 16:2 17:1 18:1 19:1 20:1 21:3 22:1 23:1 24:1 25:1 26:1 27:1 28:1 29:1 30:1 31:1 32:1 33:1 34:1 35:1 36:2 37:1 38:1 39:1 40:1 41:1 42:2 43:2 44:1 45:1 46:1 47:1 48:1 49:2 50:1 51:1 52:1 53:1 54:1 55:2 56:2 57:1 58:1 59:1 60:1 61:1 62:1 63:1 64:1 65:1'), Example('1 3:12 4:23 8:1 9:4 12:13 17:1 21:2 23:4 27:2 36:7 39:1 41:1 44:1 46:1 51:5 56:2 58:1 81:1 83:1 87:1 91:7 119:1 145:2 150:1 167:1 175:3 185:1 196:1 206:2 210:1 226:1 228:2 229:6 243:1 244:3 259:1 289:1 293:1 309:1 320:1 327:3 396:1 409:2 428:1 445:1 454:2 465:3 467:1 482:2 553:1 555:1 567:1 570:2 577:11 580:1 586:3 590:1 699:1 720:1 723:1 795:3 827:1 870:1 903:1 944:3 978:1 991:15 1001:1 1006:1 1014:1 1015:1 1016:1 1038:3 1039:1 1092:2 1098:1 1102:1 1109:1 1125:1 1247:1 1282:1 1411:1 1451:3 1465:1 1511:1 1555:1 1556:1 1557:1 1618:1 1645:1 1768:1 1846:1 1889:2 1945:1 1977:1 2161:1 2164:1 2218:1 2233:1 2284:1 2291:1 2297:1 2322:1 2544:1 2680:6 2910:1 2911:1 3030:2 3072:1 3094:1 3162:1 3222:2 3357:1 3615:1 3661:1 3830:1 3914:3 4055:1 4238:1 4569:1 4574:1 4579:1 4590:1 4755:1 5114:1 5257:1 5493:1 6512:1 6896:1 8582:1 8919:1 10156:1 10419:1 10691:1 10790:1 13029:1 14475:1 16694:1 17727:1 18027:1 20471:2 20713:1 20778:1 21313:4 27125:1 43710:1 50311:1 51807:1 60407:1 60408:1 60409:1 60410:1 60411:1'), Example('1 3:4 4:7 8:1 9:2 12:3 36:2 41:3 46:1 51:2 58:1 91:1 97:1 107:2 123:1 167:1 177:2 196:1 197:1 222:4 240:3 255:1 265:1 268:3 277:1 383:1 430:1 454:1 541:1 542:1 555:1 568:1 570:1 601:1 834:1 853:1 1184:1 1255:2 1270:3 1439:1 1534:1 1538:1 1539:1 1545:1 1674:3 1915:1 2029:2 2192:1 2802:2 2867:1 2980:1 3364:1 3378:1 3891:1 3937:1 4491:1 5109:1 5341:1 6195:1 6252:1 6380:1 6383:1 6384:1 6554:1 9377:1 10843:1 10853:2 16674:2 29444:1 29622:1 32745:2 44414:1 56104:1')]
test = load_data('../data/arxiv/arxiv.test')
print bc.predict_all(test)
# print bc.predict_all(test, cost_sensitive=True)