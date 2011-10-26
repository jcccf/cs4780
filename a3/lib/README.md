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
* FasterPerceptron.py - a supposedly faster implementation of perceptron - this is the one you generally want to use
* FastPerceptron.py - a faster implementation of perceptron - this is what you want to use.
* LightRunner.py - a script that calls svm_classify and svm_learn
* Loaders.py - class to load training examples
* main.py - does part_a
* part_a.py - does plotting for part a
* part_b.py - does plotting for part b
* part_c - does part c
* part_c2.py - does plotting for part c
* Plotter.py - plotting functions
* ProgressBar.py - a useful progress bar