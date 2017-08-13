# Shortest Path Trees and Reach in Road Networks

Louis Abraham and Sayuli Drouard
January 2017

Assignment url: https://www.irif.fr/~kosowski/INF421-2016/problem.html


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

- Benjamin Doerr for the course
- Adrian Kosowski for the assignment topic and the evaluation
- The whole team of [Road/Transportation network project at Gang](https://files.inria.fr/gang/road/).
