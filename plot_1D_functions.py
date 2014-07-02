
import sys
import matplotlib.pyplot as plt
import numpy as np

def mean(values):
	return sum(values)/float(len(values))


def average_values(values, window_size):

	n_values = len(values)
	n_avg_values = n_values/window_size

	avg_values = [[0] * n_avg_values for i in range(n_avg_values)] #pre-allocate
	for i in xrange(n_avg_values):
		avg = mean(values[i*window_size : min((i+1)*window_size, len(values))])
		avg_values[i] = avg

	return avg_values

def read_config(argv):
	cfg = {'scaled': False, 'bar': False, 'xlabel': '', 'ylabel': '', 'mean_window': 0}

	i = 0
	while i < len(argv):
		if argv[i] == "--scaled":
			cfg['scaled'] = True
		elif argv[i] == "--bar":
			cfg['bar'] = True
		elif argv[i] == "--xlabel":
			i = i + 1
			cfg['xlabel'] = argv[i]
		elif argv[i] == "--ylabel":
			i = i + 1
			cfg['ylabel'] = argv[i]
		elif argv[i] == "--mean_window":
			i = i + 1
			cfg['mean_window'] = int(argv[i])
		
		i = i + 1

	return cfg

# remove the configuration from the files and labels
# This list comprehension almost make me cry!
sys.argv = sys.argv[1:]
files_and_labels = [x for x,i in zip(sys.argv, range(len(sys.argv))) if x[0:2] != "--" and (i == 0 or sys.argv[i-1][0:2] != "--")]

if len(sys.argv) < 3 or (len(files_and_labels) % 2) != 0:
	print "Usage: python",sys.argv[0],"[files] [labels] (options)"
	print "otions:"
	print "  --xlabel [label]"
	print "  --ylabel [label]"
	print "  --scaled - if present scale all the plots from 0 to 1"
	print "  --bar - plot the files as vertical bars"
	print "  --mean_window [size] - the size in which an average will be computed"
	exit(42)

cfg = read_config(sys.argv)

files  = files_and_labels[0:len(files_and_labels)/2]
labels = files_and_labels[len(files_and_labels)/2:]

print "files",files
print "labels",labels
print "cfg",cfg

plt.figure(facecolor='white')
plots = []

for f,i in zip(files, range(len(labels))):
	v_file = open(f)
	v_lines = v_file.readlines()

	# remove breakpoint in lines # God saves list comprehensions!
	v_lines = [line.rstrip('\n') for line in v_lines]

	values =[float(x) for x in v_lines]

	if cfg['mean_window'] > 1:
		values = average_values(values, cfg['mean_window'])

	# scaled xs from 0 to 1!
	n_values = len(values)
	xs = np.arange(n_values)

	if cfg['scaled']:
		xs = xs/float(n_values)

	if cfg['bar']:
		plt.bar(xs, values, label=labels[i])
	else:
		plt.plot(xs, values, '-', linewidth=2, label=labels[i])

ax = plt.gca()
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc=9)

if cfg['xlabel'] != '':
	plt.xlabel(cfg['xlabel'])
if cfg['ylabel'] != '':
	plt.ylabel(cfg['ylabel'])

plt.show()
print "Done!"






