from abc import ABC, abstractmethod

class Edible(ABC):
  
  @abstractmethod
  def get_energy(self) -> float:
    pass
