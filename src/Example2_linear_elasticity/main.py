import sys
sys.path.append('../')
import tensorflow as tf
physical_devices = tf.config.list_physical_devices('GPU')
try:
  tf.config.experimental.set_memory_growth(physical_devices[0], True)
except:
  # Invalid device or cannot modify virtual devices once initialized.
  pass
from pde_system_elasticity_linear import WeakPDELinearElasticity as thisPDESystem

if __name__ == '__main__':
    problem = thisPDESystem()
    problem.run()
