from SLWrapper import *

# Normalized Files
train_file = '../data/arxiv/arxiv.norm.train'
test_file = '../data/arxiv/arxiv.norm.test'
model_file = '../data/arxiv/arxiv.norm.model'
classified_file = '../data/arxiv/arxiv.norm.classified'

# Unnormalized Files
train_file2 = '../data/arxiv/arxiv.train'
test_file2 = '../data/arxiv/arxiv.test'
model_file2 = '../data/arxiv/arxiv.model'
classified_file2 = '../data/arxiv/arxiv.classified'

# # PART A I
# learn(train_file, model_file)
# c = classify(test_file, model_file, classified_file)
# print get_accuracy(c)

# # Picked some C so now test on the test file (normalized)
# learn(train_file, model_file, c=1)
# c = classify(test_file, model_file, classified_file)
# print get_accuracy(c)
# print get_false_posneg(test_file, classified_file)


# # PART A II+
# for c in [0.001, 0.01, 0.1, 1]:
#   print c
#   print get_cross_val_accuracy(train_file2, 4, c)

# Picked some C so now test on the test file (unnormalized)
learn(train_file2, model_file2, c=0.01)
c = classify(test_file2, model_file2, classified_file2)
print c
print get_accuracy(c)
print get_false_posneg(test_file2, classified_file2)


# # PART D
# for c in [0.001, 0.01, 0.1, 1]:
#   print c
#   print get_cross_val_accuracy(train_file, 4, c=c, j='10')
  
# for c in [0.1]:
#   learn(train_file, model_file, c=c, j='10')
#   c = classify(test_file, model_file, classified_file)
#   print get_accuracy(c)
#   print get_false_posneg(test_file, classified_file)