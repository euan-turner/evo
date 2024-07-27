from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

import numpy as np
import numpy.typing as npt

from src.traits.Edible import Edible
from src.traits.Objective import Objective


@dataclass
class OrganismGenes:
  size: float
  speed: float 
  perception: float 
  reach: float
  lifespan: int 

class Organism(ABC):

  @abstractmethod
  def __init__(self, pos: npt.NDArray[np.float64]) -> None:
    self.pos = pos

  @abstractmethod 
  def set_initial_position(self, pos: npt.NDArray[np.float64]):
    pass 

  @abstractmethod
  def mutate(self, seed: int) -> 'Organism':
    pass

  @abstractmethod
  def age(self) -> 'Organism':
    pass

  @abstractmethod 
  def get_size(self) -> float:
    pass 

  @abstractmethod
  def get_speed(self) -> float:
    pass 

  @abstractmethod
  def set_speed(self, speed: float) -> None:
    pass 

  @abstractmethod
  def get_perception(self) -> float:
    pass 

  @abstractmethod
  def set_perception(self, perception: float) -> None:
    pass

  @abstractmethod 
  def get_reach(self) -> float:
    pass 

  @abstractmethod
  def get_lifespan(self) -> float:
    pass

  def get_genes(self) -> OrganismGenes:
    return OrganismGenes(
      size = self.get_size(),
      speed = self.get_speed(),
      perception = self.get_speed(),
      reach = self.get_reach(),
      lifespan = self.get_lifespan()
    )
  
  @abstractmethod 
  def is_alive(self) -> bool:
    pass 

  @abstractmethod
  def is_active(self) -> bool:
    pass

    """ move_to:
    Should:
    - Update creature's internal position
    - Apply energy cost
    - Die if out of energy
    """
  @abstractmethod
  def move_to(self, pos: npt.NDArray[np.float64]) -> bool:
    pass

  @abstractmethod 
  def get_position(self) -> npt.NDArray[np.float64]:
    pass

  @abstractmethod 
  def get_direction(self) -> npt.NDArray[np.float64]:
    pass 

  @abstractmethod
  def get_objective(self) -> Optional[Objective]:
    pass 

  @abstractmethod 
  def set_objective(self, objective: Objective) -> None:
    pass 

  @abstractmethod
  def clear_objective(self) -> None:
    pass 

  def can_see(self, point: npt.NDArray[np.float64]) -> bool:
    return np.linalg.norm(point - self.pos) <= self.get_perception()

  def can_reach(self, point: npt.NDArray[np.float64]) -> bool:
    return np.linalg.norm(point - self.pos) <= self.get_reach()

  @abstractmethod 
  def eat(self, food: Edible) -> None:
    pass
    
  @abstractmethod
  def get_energy_left(self) -> int:
    pass