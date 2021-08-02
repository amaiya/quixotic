# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_optimization.quantum_annealing.ipynb (unless otherwise specified).

__all__ = ['QuantumAnnealer', 'SUPPORTED_TASKS', 'QA_LOCAL']

# Cell

import networkx as nx
import warnings

# dwave imports
import dwave_networkx as dnx
from dwave.system.composites import EmbeddingComposite

# local imports
from .base import QuantumOptimizer, DEFAULT_LOCAL_SIMULATOR


SUPPORTED_TASKS = {'maximum_clique': dnx.maximum_clique,
                  'minimum_vertex_cover': dnx.min_vertex_cover,
                   'minimum_weighted_vertex_cover' :dnx.min_weighted_vertex_cover,
                   'maximum_independent_set': dnx.maximum_independent_set,
                   'maximum_weighted_independent_set' : dnx.maximum_weighted_independent_set,
                   'maximum_cut' : dnx.maximum_cut,
                   'weighted_maximum_cut' : dnx.weighted_maximum_cut,
                   'traveling_salesperson' : dnx.traveling_salesperson
                  }
QA_LOCAL = 'dwave-neal'

class QuantumAnnealer:

    """quantum-based combinatorial optimization with Amazon Braket


    Usage:

    ```python
    >>> qo = QuantumAnnealer(g,
                            task='maximum_clique',
                            device_name='local',     # uses local simulator solver
                            device_arn='device_arn', # only needed if not local
                            s3_folder='s3_folder')   # only needed if not local
        qo.execute()
        results = qo.results()
    ```

    **Parameters:**

    * **g** : a networkx Graph object
    * **task** : one of {'maximum_clique'}
    * **device_name** : one of {'braket.local.qubit', 'braket.aws.qubit'}
    * **device_arn** : Device ARN. Only required if name != 'local'.
    * **s3_folder** : S3 folder. Only required if name != 'local'.
    """
    def __init__(self, g, task=None,
                 local=True, device_arn=None, s3_folder=None):
        """
        constructor
        """
        # error checks
        if task not in SUPPORTED_TASKS: raise ValueError(f'task {task} is not supported. ' +\
                                                         f'Supported tasks: {list(SUPPORTED_TASKS.keys())}')
        if not local and (device_arn is None or s3_folder is None):
            raise ValueError('device_arn and s3_folder are required if using managed AWS device')
        if local and (device_arn is not None or s3_folder is not None):
            warnings.warn('local=True is being ignored since device_arn and s3_folder exist. ')
        if not isinstance(g, nx.Graph): raise ValueError('g must be instance of networkx.Graph')

        # input vars
        self.g = g
        self.task = task
        self.local = local
        self.device_arn = device_arn
        self.s3_folder = s3_folder


        # computed vars
        self._last_result = None
        self._exec_called = False

    @staticmethod
    def supported_tasks():
        """
        Prints supported tasks (valid values for the `task` parameter).
        """
        for task in SUPPORTED_TASKS:
            print(task)

    def execute(self, verbose=1, **kwargs):
        """
        Approximate a solution to given task.
        Simulated Annealing is used when `QuantumAnnealer.local=True`.
        Quantum Annealing is used when `QuantumAnnealer.local=False`.
        """

        # setup sampler
        if self.local:
            if self.g.number_of_nodes() < 18:
                from dimod.reference.samplers import ExactSolver
                sampler = ExactSolver()
            else:
                import neal
                sampler = neal.SimulatedAnnealingSampler()
        else:
            bracket_sampler = BraketSampler(self.s3_folder, self.device_arn)
            sampler = EmbeddingComposite(braket_sampler)

        # generate approximation
        kwargs = {}
        if 'weighted' in 'self.task': kwargs['weight'] = 'weight'
        apx_fn = SUPPORTED_TASKS[self.task]
        if self.local:
            result = apx_fn(self.g, sampler, **kwargs)
        else:
            kwargs['resultFormat'] = 'HISTOGRAM'
            #result = apx_fn(self.g, sampler, resultFormat="HISTOGRAM")
            result = apx_fn(self.g, sampler, **kwargs)


        self._last_result = result
        self._exec_called = True
        return self

    def results(self, **kwargs):
        """
        Return approximated solution
        """
        if not self._exec_called: raise Exception('The execute method must be called first.')
        if 'return_probs' in kwargs and kwargs['return_probs']:
            warnings.warn('return_probs not currently supported in QuantumAnnealer, '+\
                          'so returning None for second return value.')
            return self._last_result, None
        else:
            return self._last_result


    def plot_samples(self, probs):
        """
        Plot sample for toy problems for testing purposes.
        """
        raise NotImplemented('QuantumAnnealer does not currently support plot_samples.')
