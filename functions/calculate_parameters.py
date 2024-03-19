import numpy as np
import astropy.units as au
import astropy.constants as ac


def calculate_asini_from_RV(ecc,K,Porb):
    # Calculates asini according to RV variations
    # K in km/s
    # Porb in days
    # Returns asini in Rsun
    # eq --> asini = (1.9758e-2) * sqrt(1 - ecc^2) * K * Porb
    return (1.9758e-2) * np.sqrt(1-ecc**2) * K * Porb


def calculate_K_from_RV(ecc,asini,Porb):
    # Calculates semi-amplitude K according to asini
    # asini in Rsun
    # Porb in days
    # Returns K in km/s
    # eq --> K = asini / [(1.9758e-2) * sqrt(1 - ecc^2) * Porb]
    return asini / ( (1.9758e-2) * np.sqrt(1-ecc**2) * Porb )


def calculate_msin3i(ecc,K1,K2,Porb):
    # Calculates msin3i according to RV variations
    # K in km/s
    # Porb in days
    # Returns m1sin3i and m2sin3i in Msun
    # eq --> m_1_sin3i = (1.0361e-7) * (1 - ecc^2)^1.5 * (K1+K2)^2 * K2 * Porb
    # eq --> m_2_sin3i = (1.0361e-7) * (1 - ecc^2)^1.5 * (K1+K2)^2 * K1 * Porb

    m1sin3i = (1.0361e-7) * ((1-ecc**2)**1.5) * ((K1+K2)**2) * K2 * Porb
    m2sin3i = (1.0361e-7) * ((1-ecc**2)**1.5) * ((K1+K2)**2) * K1 * Porb

    return m1sin3i * au.Msun, m2sin3i * au.Msun

def calculate_amplitude_dynamical_ETV(m3,m123,P_3,P_12):
    # Calculates the dynamical contribution to the ETV
    # accordin to Eq. 72 of Borkovits 2003
    # m3 in Msun
    # m123 in Msun
    # P_12 in days
    # P_3 in days
    # returns amplitude of the dynamical perturbation in minutes

    return ((3./(np.pi*8.)) * (m3 / m123) * (P_12**2/P_3) * au.day).to('minute')


if __name__=='__main__':

    # Parameters of the wide orbit -- AB + C
    # AB is the 1.1047 d EB
    # C is an early B-type star
    P_AB_C = 51.928 * au.d
    t0_AB_C = 1880.485 # BJD - 2454833.
    omega_AB_C = -1.0125 # radians
    ecc_AB_C = 0.318
    gamma_AB_C = -41.38 * au.km / au.second

    K_C = 66.5 * au.km / au.second
    a_C_sini = calculate_asini_from_RV(ecc_AB_C,K_C.value,P_AB_C.value)*au.Rsun

    a_AB_sini = 96.05 * au.Rsun
    K_AB = calculate_K_from_RV(ecc_AB_C,a_AB_sini.value,P_AB_C.value) * au.km / au.second

    m1sin3i,m2sin3i = calculate_msin3i(ecc_AB_C,K_C.value,K_AB.value,P_AB_C.value)
    print('M1sin3i = {}'.format(m1sin3i))
    print('M2sin3i = {}'.format(m2sin3i))
    print('a_ABC = {}'.format( (a_AB_sini + a_C_sini).to('AU')))
