# AnalysisofAlgos-Proj1
This is the first project for Analysis of Algorithms. It consists of creating algorithms to find prime numbers less then an input number

TO RUN
-----------------
--run it with user inputed values

  python GCD.py

--run it with average times report

  python GCD.py --benchmark

--run it with bokeh report graphs
  * requires bokeh -> (linux: sudo pip install bokeh)

  python GCD.py --benchmark --print-to-bokeh






Directions

12. Input two integers and compute their greatest common
divisor. This is to be done two ways:

a) Use Euclid's GCD algorithm (page 935 of 3rd edition CLRS text)
b) Factor each integer into its prime factors
   and determine if there are any factors in common.
   Factoring should be done by modification of the
   "trial division" algorithm (see Project 1a above for trial division)
   Note: If you wish, you can simply factor one of the integers and test
if each is a factor of the other (rather than factoring each and then
combing the two lists for all common elements).

Run each program for a variety of inputs (including integers as large as
practical) and report the running times for each (you may wish to compute
running times with library function or simply by using a watch with a
secondhand). E-mail me your source code and a brief text summary of your
experimental results.
