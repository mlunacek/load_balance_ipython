load_balance_ipython
====================

An abstraction of the IPython Parallel task interface

This is a simple class that create the IPython profile to launch engines on a cluster using SSH and the nodes in a PBS_NODEFIILE.  Please see the example. The default processors per node is 12, but this can be changed in three ways:

* edit the loadbalance.py
* pass a different value when instantiating the class
* use the environmental variable PPN: e.g. export PPN=12



