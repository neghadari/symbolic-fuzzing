""" Symbolic Fuzzer Float

Before Use make sure to install the fuzzingbook package.

An Advanced Fuzzer is initialized. Data is Generated and stored. The test function is called
using the generated data, and the resutls are printed. 
ArcCoverage is used as a tracer that uses data generated by the fuzzer to determine how much
of the paths are reachable. 
Control flow graph is generated and viewed.
To generate and view the graph, change the code on line 41 and insert unique filename and
directory.
Imported Function 'paths_and_constraints' is called to print the paths and their constraints.
"""

from fuzzingbook.ConcolicFuzzer import ArcCoverage
from utils.ModifiedSymbolicFuzzer import *
from fuzzingbook.ControlFlow import PyCFG, CFGNode, to_graph, gen_cfg
import inspect
from graphviz import Source, Graph

from utils.paths_and_constraints import paths_and_constraints
from input_functions.abs_value import abs_value

def symbolic_fuzzer_abs():
    """Prints fuzzing data and genertes Control Flow Graph

    Args: 
        None
    """
    
    sym_fuzzer = AdvancedSymbolicFuzzer(
        abs_value,
        max_tries = 10,
        max_iter = 10,
        max_depth =10
    )

    data = []

    for i in range(10):
        r = sym_fuzzer.fuzz()
        data.append((r['x'].as_fraction()))
        v = abs_value(data[-1])
        print(r, "Result", repr(v))

    with ArcCoverage() as cov:
        for x in data:
            abs_value(x)

    graph = Source(to_graph(gen_cfg(inspect.getsource(abs_value)), arcs= cov.arcs()))
    graph.view(filename="cfg.gv", directory="E:\dir\graphs")

    paths_and_constraints(abs_value)


