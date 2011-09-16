from NearestNeighbors import *
from Loaders import *
from optparse import OptionParser
	
# Options
parser = OptionParser()
parser.add_option("-r", "--train", type="string", dest="train", default="cal.train", help="Training Data File")
parser.add_option("-t", "--test", type="string", dest="test", default="cal.test", help="Test Data File")
parser.add_option("-k", "--k", type="int", dest="k", default=1, help="Number of Neighbors")
parser.add_option("-w", "--weighted", action="store_true", dest="weighted", default=False, help="Run Weighted Version?")
parser.add_option("-n", "--normalize", action="store_true", dest="normalized", default=False, help="Normalize Data?")
(options, args) = parser.parse_args()

print "Loading '%s' as training set and '%s' as test set..." % (options.train,options.test)
knn = load_training_data(options.train)
test_data = load_test_data(options.test)

if options.normalized:
	print "Normalizing..."
	knn.normalize()
	test_data = knn.normalize_examples(test_data)

# print knn.examples[0].features
# print test_data[0].features
print "Testing with k=%d, weighted=%s" % (options.k, options.weighted)
print knn.rmse(test_data, k=options.k, is_weighted=options.weighted)