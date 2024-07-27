from dataclasses import dataclass

import numpy as np
import numpy.typing as npt


@dataclass
class Objective:
  pos: npt.NDArray[np.float64]