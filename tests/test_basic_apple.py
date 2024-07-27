
from src.simulation.BasicApple import BasicApple

def test_iter_count_zero_init():
  ba = BasicApple()
  assert ba.get_num_iterations() == 0

def test_next_incs_iter_count():
  ba = BasicApple()
  ba.run_next_iteration()
  assert ba.get_num_iterations() == 1
