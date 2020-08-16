#!/usr/bin/env python

# * ---------------------- * #
# * src/quantum_pi/main.py * #
# * ---------------------- * #

"""
This file that can serves as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
        quantum-pi = quantum_pi.main:run

Then run `python setup.py install` which will install the command `quantum-pi`
inside your current environment.
"""

# * ------- * #
# * IMPORTS * #
# * ------- * #

import argparse
import sys
import logging

from quantum_pi import __version__

# from IPython.display import clear_output
# from  qiskit import *
# from qiskit.visualization import plot_histogram
# import numpy as np
# import matplotlib.pyplot as plotter
# from qiskit.tools.monitor import job_monitor
# Visualisation settings
# import seaborn as sns, operator
# sns.set_style("dark")


# * --------- * #
# * CONSTANTS * #
# * --------- * #

__author__ = "Patrick Evans"
__copyright__ = "Patrick Evans"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

# pi = np.pi


# * --------- * #
# * FUNCTIONS * #
# * --------- * #

## Code for inverse Quantum Fourier Transform
## adapted from Qiskit Textbook at
## qiskit.org/textbook
def qft_dagger(circ_, n_qubits):
    """n-qubit QFTdagger the first n qubits in circ"""
    for qubit in range(int(n_qubits/2)):
        circ_.swap(qubit, n_qubits-qubit-1)
    for j in range(0,n_qubits):
        for m in range(j):
            circ_.cu1(-np.pi/float(2**(j-m)), m, j)
        circ_.h(j)


## Code for initial state of Quantum Phase Estimation
## adapted from Qiskit Textbook at qiskit.org/textbook
## Note that the starting state is created by applying
## H on the first n_qubits, and setting the last qubit to |psi> = |1>

def qpe_pre(circ_, n_qubits):
    circ_.h(range(n_qubits))
    circ_.x(n_qubits)

    for x in reversed(range(n_qubits)):
        for _ in range(2**(n_qubits-1-x)):
            circ_.cu1(1, n_qubits-1-x, n_qubits)


## Run a Qiskit job on either hardware or simulators

def run_job(circ_, backend_, shots_=1000, optimization_level_=0):
    job = execute(circ_, backend=backend_, shots=shots_, optimization_level=optimization_level_)
    job_monitor(job)
    return job.result().get_counts(circ_)


def parse_args(args):
    """Parse command line parameters

    Args:
    	args ([str]): command line parameters as list of strings

    Returns:
    	:obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Just a Fibonacci demonstration")
    parser.add_argument(
        "--version",
        action="version",
        version="puantum-pi {ver}".format(ver=__version__))
    parser.add_argument(
        dest="n",
        help="n-th Fibonacci number",
        type=int,
        metavar="INT")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
    	loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
    	args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    # print("The {}-th Fibonacci number is {}".format(args.n, fib(args.n)))
    _logger.info("Script ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()

# EOF #
