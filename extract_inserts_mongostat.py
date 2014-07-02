
import sys
import matplotlib.pyplot as plt

if len(sys.argv) != 3:
	print "Usage: python",sys.argv[0],"mongostat-results.txt [option]"
	print "   [option] = plot if one wants to plot OR"
	print "   [option] = out_file.txt if one wants to save results"
	exit(42)

stat_file = open(sys.argv[1])
stat_lines = stat_file.readlines()

# the id of the field we want to extract, in this
# case the insert field is the first
id_field = 0
values = []

for line in stat_lines:
	fields = line.split(" ")

	# filter list to remove empty strings	
	fields = filter(None, fields);
	if fields[id_field].isdigit():
		values.append(int(fields[id_field]))
	else:
		pass # skiping this line


if sys.argv[2] == "plot":
	xs = range(len(values));
	print values
	plt.plot(xs, values, '-', linewidth=2);
	plt.show()
else:
	out_filename = sys.argv[2];
	out_file = open(out_filename, 'w');
	for v in values:
		out_file.write(str(v)+'\n');


print "Done!"






