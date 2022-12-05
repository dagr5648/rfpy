'''
This script is used to estimate common transmission line parameters 

'''

import numpy as np
import unit_conversions


def surface_resistance(f,mu,):
    pass

def skin_depth():
    pass
    

def coax_rlcg(a,b,f,material,dielectric,verbose = False):
    '''

    Parameters
    ----------
    a : outer radius of center conductor (m)
    b : inner radius of outer conductor(m).
    f : frequency to calculate at (Hz)

    material : str of tline material name, indexes into material library.
    dielectric : str of dialectric material name, indexes into material library .

    Returns
    -------
    R,L,C,G circuit parameters (if verbose = False)
    R,L,C,G,Rs,mat_props (if verbose =  True)

    '''
    pass

def two_wire_rlcg(a,D,material,dialectric):
    pass

def parallel_plate_rlcg(w,d,material,dialectric):
    pass