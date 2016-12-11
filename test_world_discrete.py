#!/usr/bin/env python3

import numpy as np
from particlefilter import ParticleFilter

def get_true_obs(state):
    if state < 20:
        return 5
    elif 20 <= state < 60:
        return state
    elif 60 <= state < 80:
        return 10
    else:
        return 20

def p_particle(state, sensor_reading):
    """
    Weight using Gaussian kernel
    """
    variance = 5
    return np.exp(-(get_true_obs(state) - sensor_reading) ** 2 / (2 * variance)) \
        if 0 <= state < 100 else 0

def next_particle(state, prop_param):
    """
    Sample new state from Gaussian around new expected location. 
    prop_param: predicted change in state
    """
    sigma = 3
    expected_state = state + prop_param
    return int(np.random.normal(expected_state, sigma))

n_particles = 20
pf = ParticleFilter(
    p_particle,
    next_particle,
    np.random.choice(100, size=n_particles)
)

true_state = 2
while True:
    print('True state: {}'.format(true_state))
    print('Particles: {}'.format(sorted(pf.particles)))
    print('=========\n')

    obs = np.random.normal(get_true_obs(true_state), 5)
    print('Observation: {}'.format(obs))
    prop_param = int(input('Enter expected change in state: '))
    true_state = max(min(true_state + prop_param, 99), 0)

    pf.observe(obs, prop_param)