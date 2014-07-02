mongostat_plotter
=================

Make nice plots using the mongostat output.

This project was developed in order to process and visualize the mongostat results of a series of stress tests perfomed. There is
two scripts that should be run.

```extract_inserts_mongostat.py```: extract the column corresponding to the inserts per second registered by mongostat. This can be easily modified to extract other informations.

```plot_1D_functions.py```: this is used to get the information of an 1D curve and plot using matplotlib. This plots can be customized, see the options section

Running & Options
===========
```
Usage: python extract_inserts_mongostat.py mongostat-results.txt [option]
	[option] = plot if one wants to plot OR
	[option] = out_file.txt if one wants to save results
```

Being the output file called ```out_inserts.txt```, you can plot them using the
script ```python plot_1D_functions.py``` as follows:

```
Usage: python plot_1D_functions.py [files] [labels] (options)
     options:
        --xlabel [label]
		--ylabel [label]
		--scaled - if present scale all the plots from 0 to 1
		--bar - plot the files as vertical bars
		--mean_window [size] - the size in which an average will be computed
```

Sample:
![Alt text](https://raw.githubusercontent.com/rbsdev/mongostat_plotter/master/sample/huge_hour.png "Example of plotting inserts in mongoDB")


Enjoy!