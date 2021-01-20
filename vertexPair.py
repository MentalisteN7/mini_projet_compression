# from dataclasses import dataclass, field
# from typing import Any
import numpy as np
# 
# @dataclass(order=True)
# class PrioritizedItem:
#     priority: float
#     item: Any=field(compare=False)

class vertexPair:
    vindices : tuple
    cost : float
    v_bar : np.ndarray
    
    def __init__(self, indices):
        self.vindices = indices
        

