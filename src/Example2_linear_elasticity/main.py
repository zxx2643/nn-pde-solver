import sys
sys.path.append('../')
from pde_system_elasticity_linear import WeakPDELinearElasticity as thisPDESystem

if __name__ == '__main__':
    problem = thisPDESystem()
    problem.run()
