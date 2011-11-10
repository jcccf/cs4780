import operator

y_p = {"a": 0.1, "n": 0.4, "o":0.2, "t":0.3}

yy_p = { 
	"a": {"a": 0.05, "n": 0.35, "o":0.1, "t":0.4},
	"n": {"a": 0.1, "n": 0.05, "o":0.5, "t":0.1},
	"o": {"a": 0.25, "n": 0.5, "o":0.1, "t":0.4},
  "t": {"a": 0.6, "n": 0.1, "o":0.3, "t":0.1},
}

xy_p = {
  "A": {"a":0.4, "n":0.3, "o":0.1, "t":0.1},
  "T": {"a":0.2, "n":0.1, "o":0.1, "t":0.4},
  "N": {"a":0.1, "n":0.4, "o":0.1, "t":0.1},
  "Y": {"a":0.2, "n":0.1, "o":0.2, "t":0.3},
  "W": {"a":0.1, "n":0.1, "o":0.5, "t":0.1},
}

def viterbi(xs):
  # Initialize arrays
  T = [dict([(a,0.0) for a in y_p.keys()]) for j in range(len(xs))] # Values
  T_prev = [dict([(a,None) for a in y_p.keys()]) for j in range(len(xs))] # Back-pointers
  i = 0
  for c in xs:
    if i == 0: # START which is P(y_0) * P(x_0|y_0)
      for k in T[0].keys():
        T[0][k] = y_p[k] * xy_p[c][k]
    else: # Then do prev * P(x_i|y_i) * P(y_i|y_{i-1})
      for k2 in y_p.keys():
        T_prev[i][k2], T[i][k2] = max([(k,T[i-1][k]* xy_p[c][k2] * yy_p[k2][k]) for k in y_p.keys()], key=operator.itemgetter(1))
    i += 1
  
  # Build up prediction
  i -= 1
  index = max(T[i].iteritems(), key=operator.itemgetter(1))[0] # Get final character
  result = [index]
  while i > 0: # Get previous characters by traversing back-pointers
    index = T_prev[i][index]
    result.append(index)
    i -= 1
  result.reverse() # Reverse the array
  
  # Print tables nicely
  print "Table of probabilities for partial paths"
  transp = dict([(a,[]) for a in y_p.keys()])
  for t in T:
    for k,v in t.iteritems():
      transp[k].append(v)
  for k, vs in transp.iteritems():
    s = '{}'.format(k)
    for v in vs:
      s += ' & {}'.format(v)
    s += " \\\\"
    print s
  print "Back-pointer table"
  transp = dict([(a,[]) for a in y_p.keys()])
  for t in T_prev:
    for k,v in t.iteritems():
      transp[k].append(v)
  for k, vs in transp.iteritems():
    s = '{}'.format(k)
    for v in vs:
      s += ' & {}'.format(v)
    s += " \\\\"
    print s
  print "Predicted Letters"
  print result

# Viterbi
viterbi("TWY")