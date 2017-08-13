# Shortest Path Trees and Reach in Road Networks

**Louis Abraham** and **Sayuli Drouard**

*January 2017*

Assignment url: https://www.irif.fr/~kosowski/INF421-2016/problem.html

Take a look at the [PDF report](https://github.com/louisabraham/INF421-project/blob/master/report/Report.pdf)!

# How to run

* To run `demo.py`, simply edit the parameters.

```
data:
    source file of the graph
logging:
    file where the points are logged when the logging parameter is used in the appropriate functions
timeit.activated:
    boolean that toggle the display of timings to stderr
```

* `multiple_example.py` is a simple example over a graph with multiple shortest paths, it should be run as provided, and is really useful to test some modifications of the functions.

* `test_reach.py` uses almost the same parameters as `demo.py`. For the others:

```
tests:
    list of vertices we want to compute the reach
number_of_random_tests:
    no explication needed
```

* `compute_reach.py` computes the reaches of random vertices from the data parameter and prints the result in the log file. You can give the number of random vertices as parameter or input it by hand.

* `launch.sh a b` launches a independant instances of compute_reach.py with the parameter b.

* `plot.py` reads the logfile filled by compute_reach to show histograms.

# Thanks

- [Benjamin Doerr](http://people.mpi-inf.mpg.de/~doerr/) for the course [INF421: Design and Analysis of Algorithms](https://www.enseignement.polytechnique.fr/informatique/INF421/).
- [Adrian Kosowski](https://www.irif.fr/~kosowski/) for the assignment topic and the evaluation.
- The whole team of [Road/Transportation network project at Gang](https://files.inria.fr/gang/road/).
