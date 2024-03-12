"""
Module to manipulate matrices
"""

import numpy as np


def add(X, Y) -> np.ndarray:
    """Adds 2 matrices"""
    return np.add(X, Y)


def mat_mul(X, Y) -> np.ndarray:
    """Multiplies 2 matrices"""
    return np.matmul(X, Y)


def identity(order: int) -> np.ndarray:
    """Returns the identity matrix"""
    return np.identity(order)
