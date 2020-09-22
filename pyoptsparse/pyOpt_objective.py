#!/usr/bin/env python
import numpy as np

# =============================================================================
# Objective Class
# =============================================================================
class Objective(object):
    def __init__(self, name, scale=1.0):
        """
        This class holds the representation of a pyOptSparse objective.

        Parameters
        ----------
        name : str
            Name of this objective

        scale : float
            Scaling factor for objective. This does not change the actual
            optimization problem, but may be used to give a more
            human-meaningful value

        See Also
        --------
        Optimization.addObj : for the full documentation
        """
        self.name = name
        self.value = 0.0
        self.optimum = 0.0
        self.scale = scale

    def __str__(self):
        """
        Structured Print of Objective
        """
        res = "        Name        Value        Optimum\n"
        res += f"	 {str(self.name).center(9)}"
        res += f"{np.real(self.value):12g}  {np.real(self.optimum):12g}\n"

        return res
