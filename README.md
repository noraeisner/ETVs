# Eclipse Timing Variations (ETVs)

Collaborator: Cole Johnston (Max Planck Institute, Garching) 

Code to search for ETVs, which are deviations from a strictly linear ephemeris of the eclipsing binary, that can be used to detect or study additional gravitating bodies in a system. While the midpoint of eclipses of an isolated eclipsing binary are expected to occur at regular time intervals, perturbations from additional bodies, such as in a hierarchical triple system, can result in periodic variations in the times between consecutive eclipses.

Teh first code (extraction) generates a model of the primary eclipse by fitting a trapezoid or coshgauss (the shapes found to best represent the eclipses) to the smoothed, phase folded, and subsequently binned TESS light curve. The best-fit model generated from the phase folded data is then fit to each individual primary transit where the only two free model parameters is the time of the eclipse and the slope of an underlying linear trend. The latter is to allow for systematic effects that change the slope of the eclipse. The same methodology is independently carried out for the secondary eclipses.

The fit to the phase folded data and to all of the individual eclipses, including both the primary and the secondary eclipses, are optimised using an MCMC approach using the exoplanet library.

The second code (modeling) jointly models  ETV and the RV signals assuming
that they are physically associated as a triple system. There are two main effects responsible for deviations from strict periodicity in eclipse timings: the light travel time effect (LTTE; geometrical contribution) and the dynamical effect. The former is a result of a change in projected distance from the centre of mass of the binary
to that of the triple. The dynamical effect, on the other hand, results from physical changes in the orbit of the binary system due to the gravitational influence of the third body (Borkovits et al., 2003). Modelling of the LTTE and dynamical ETVs allows us to derive properties including the mass ratio of the tertiary to the total mass of the system (mC/mABC), the eccentricity of the tertiary, and the mutual inclination between the orbital plane of the binary and the orbital plane of the tertiary.

The model optimisation is carried out using a No U-Turn Sampling (NUTS;
Hoffman & Gelman, 2011) Hamiltonian Monte Carlo (HMC) approach. In short,
HMC is a class of MCMC methods used to numerically approximate a posterior
probability distribution. However, whereas traditional MCMC techniques use
a stochastic walk to explore a given n-dimensional parameter space, the HMC
algorithm makes use of a Hamiltonian description of probability distribution in order to more directly sample the posterior probability distribution of a set of model parameters, Θ, given by Bayes’ theorem. While the standard HMC approach requires a manual fine-tuning of the number of steps and step sizes in which the system is evolved, making it very inefficient, the NUTS HMC sampler evolves the system until the proposed location starts to revert towards the initial location.

This library contains generalized codes that can be adapted to extract ETV from TESS data and to carry out a joint model or ETV and RV data. Furthermore, there are specific examples of where these codes were used to analyse TIC 470710327 a hierarchical triple star system. 
