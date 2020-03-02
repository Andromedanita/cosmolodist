import numpy as np
from scipy import integrate

def DH(h):
    '''
    unit is Mpc
    '''
    return 3000 / h 



def E(Omegam, Omegal, Omegak,  z):
    return np.sqrt( (Omegam * (1+z)**3) + (Omegak * (1+z)**2 ) + Omegal )
    
def Dc_integrand(Omegam, Omegal, Omegak, z):
    return 1./E(Omegam, Omegal, Omegak, z)


def Dc(Omegam, Omegal, Omegak, h, z):
    
    def integrand(Omegam, Omegal, Omegak, z):
        return 1./E(Omegam, Omegal, Omegak, z)

    intg, err = integrate.quad(integrand, 0, z, args=(Omegam, Omegal, Omegak))
    return DH(h) * intg


def com_dist(Omegam, Omegal, Omegak, h, z):
    if Omegak > 0:
        return (DH(h) /np.sqrt(Omegak)) * np.sinh(np.sqrt(Omegak) * Dc(Omegam, Omegal, Omegak, h, z)/DH(h))
        
    elif Omegak == 0:
        return Dc(Omegam, Omegal, Omegak, h, z)

    elif Omegak < 0:
        return (DH(h)/np.sqrt(Omegak)) * np.sin(np.sqrt(Omegak) * Dc(Omegam, Omegal, Omegak, h, z)/DH(h))
