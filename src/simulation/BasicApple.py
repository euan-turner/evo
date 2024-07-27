from ..traits.Simulation import Simulation

class BasicApple(Simulation):

  def __init__(self):
    self.num_iterations = 0

  def run_next_iteration(self) -> None:
    self.num_iterations += 1

  def get_num_iterations(self) -> int:
    return self.num_iterations
  
  def get_iteration_stats(self, iter: int) -> any:
    pass