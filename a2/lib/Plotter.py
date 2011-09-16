import matplotlib.pyplot as plt

# Plot y against log x (semi-log plot)
def plot_semilog(name, dict, xlabel='', ylabel='', title='', linetype='k'):
	plt.clf()
	if len(xlabel) > 0:
		plt.xlabel(xlabel)
	if len(ylabel) > 0:
		plt.ylabel(ylabel)
	if len(title) > 0:
		plt.title(title)
		
	dicty = zip(*sorted(dict.iteritems()))
	plt.semilogx(dicty[0], dicty[1], linetype)
	plt.savefig('../data/images/%s.eps' % name)

# Plot log y against log x (log-log plot)
def plot_loglog(name, dict, xlabel='', ylabel='', title='', linetype='k'):
	plt.clf()
	if len(xlabel) > 0:
		plt.xlabel(xlabel)
	if len(ylabel) > 0:
		plt.ylabel(ylabel)
	if len(title) > 0:
		plt.title(title)

	dicty = zip(*sorted(dict.iteritems()))
	plt.loglog(dicty[0], dicty[1], linetype)
	plt.savefig('../data/images/%s.eps' % name)	
