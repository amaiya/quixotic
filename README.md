# Welcome to Quixotic



## What is Quixotic?
> Quixotic is a low-code library for quantum computing.

## Features
- Easy-to-apply quantum solutions to a number of combinatorial optimization problems using [QAOA](https://arxiv.org/abs/1411.4028).
- Includes out-of-the-box support for maximum clique, minimum vertex cover, and other problems.
- Supports execution using both local simulation on your laptop and managed quantum computers on [Amazon Braket](https://aws.amazon.com/braket/).

## Install

1. `pip install -U pip`
2. `pip install quixotic`

**NOTE**: Python version `>= 3.7` is required.

## Usage: Find Maximum Clique in a Graph

```python
# construct or load your input graph
import networkx as nx
n_nodes = 6
p = 0.5  # probability of an edge
seed = 1967
g = nx.erdos_renyi_graph(n_nodes, p=p, seed=seed)
positions = nx.spring_layout(g, seed=seed)
nx.draw(g, with_labels=True, pos=positions, node_size=600)
```


![png](docs/images/output_5_0.png)


```python
# approximate a solution using QAOA and extract results
from quixotic.core import QuantumOptimizer
qo = QuantumOptimizer(g, task='maximum_clique')
qo.fit()
nodes, probs = qo.results()
```

    Optimize for 10 iterations...
    [========================================] 100%	  cost: -2.4518  iteration:10

```python
# plot nodes comprising the solution
sub = g.subgraph(nodes)
nx.draw(g, pos=positions, with_labels=True)
nx.draw(sub, pos=positions, node_color="r", edge_color="r")
```


![png](docs/images/output_7_0.png)


<hr style="border:1px solid gray"> </hr>
> "Quantum computing and quantum communication are not beyond the boundaries of physics, but are still long-term prospects for use in the department.  We caution that the hyperbole surrounding these topics may be getting ahead of their military and economic utility."

**Michael D. Griffin**,  Undersecretary of Defense for Research and Engineering, during [March 2020 testimony before the HASC](https://www.defense.gov/Explore/News/Article/Article/2110617/dod-should-focus-on-short-term-goals-in-quantum-science/).
