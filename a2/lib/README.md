README
======
jc882 and sy483

Requirements
------------
* Python 2.7ish
* The matplotlib package if you wish to plot graphs

What you need to know
---------------------
* main.py is the file you want to run!
* remember to create a /data and a /data/images folder as described in the folder structure below, or you won't you'll get file access errors!
* python main.py -r "bcan.train" -t "bcan.test" -v "bcan.validate" -s 20



Folder Structure
----------------
/lib
    - all python files here and this readme
/data
    - create this folder and place all training/test data here
  /images
      - create this folder since images are output here

Notes
-----
* All files are loaded by default from the /data folder. Place training/test files in this folder!
* These should all be run from the terminal

List of Files
-------------
* DecisionTree.py - Contains the decision tree class
* Loaders.py - Contains the Example class and the function to load test data
* main.py - Main function that contains options that are callable. Use "python main.py --help" to see the available options
* part_a.py - Prints out graphs for Q2a, Q2b and Q2e
* part_c.py - Outputs results for Q2c
* part_d.py - Outputs results and graphs for Q2d
* Plotter.py - Functions for plotting graphs
* ProgressBar.py - Functions for showing a progress bar while computing