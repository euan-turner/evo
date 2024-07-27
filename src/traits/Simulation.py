from abc import ABC, abstractmethod

class Simulation(ABC):

  @abstractmethod
  def run_next_iteration(self) -> None:
    pass

  @abstractmethod 
  def get_num_iterations(self) -> int:
    pass 

  @abstractmethod
  def get_iteration_stats(self, iter: int) -> any:
    pass