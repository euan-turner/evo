from abc import ABC, abstractmethod

import numpy as np
import numpy.typing as npt

class Objective(ABC):
    
    @abstractmethod
    def get_pos(self) -> npt.NDArray[np.float64]:
        pass
