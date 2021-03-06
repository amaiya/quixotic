# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_optimization.base.ipynb (unless otherwise specified).

__all__ = ['QuantumOptimizer', 'DEFAULT_LOCAL_SIMULATOR']

# Cell

DEFAULT_LOCAL_SIMULATOR = 'local'

from abc import ABC, abstractmethod
class QuantumOptimizer(ABC):
    """
    ```
    Abstract class to preprocess data
    ```
    """
    @abstractmethod
    def execute(self, **kwargs):
        pass

    @abstractmethod
    def results(self, shots=512):
        pass
