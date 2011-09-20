from optparse import OptionParser
from Loaders import *
from DecisionTree import *
	
# Options
parser = OptionParser()
parser.add_option("-r", "--train", type="string", dest="train", default="bcan.train90", help="Training Data File")
parser.add_option("-t", "--test", type="string", dest="test", default="bcan.test", help="Test Data File")
parser.add_option("-v", "--validate", type="string", dest="validate", default="bcan.validate", help="Validation Data File")
parser.add_option("-s", "--stopping_parameter", type="int", dest="stop", default=1, help="Stopping Parameter")
(options, args) = parser.parse_args()

print "Loading\n...'%s' as training set,\n...'%s' as test set,\n...'%s' as validation set,\n...stopping parameter %d..." % (options.train, options.test, options.validate, options.stop)

training_set = load_data(options.train)
test_set = load_data(options.test)
validation_set = load_data(options.validate)
s_para = options.stop

#dt = DecisionTree(training_set, validation_set, stopping_parameter=s_para)
dt = DecisionTree(training_set, stopping_parameter= 1)
print 'test set: {} training_error : {} validation_error: {}'.format(dt.prediction_error(test_set),dt.training_error(),dt.prediction_error(validation_set))
print dt.count_nodes()

dt = dt.post_prune(validation_set)
print 'test set: {} training_error : {} validation_error: {}'.format(dt.prediction_error(test_set),dt.training_error(),dt.prediction_error(validation_set))
print dt.count_nodes()
print dt.print_tree()