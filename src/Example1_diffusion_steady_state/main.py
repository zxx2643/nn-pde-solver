import sys
sys.path.append('../')
from pde_system_diffusion_steady_state import WeakPDESteadyStateDiffusion as thisPDESystem

if __name__ == '__main__':
    problem = thisPDESystem()
    problem.run()
