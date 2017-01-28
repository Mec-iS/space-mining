total_mass_of_ss = 2.7 * 1e27
total_mass_of_terrestrial = 1.18 * 1e25
total_mass_of_gas_planets =  2.26 * 1e27
total_mass_of_minor_bodies = 4.282 * 1e26

#import scipy as sp
import numpy as np

labels = np.genfromtxt("minerals.csv", delimiter=',', usecols=0, dtype="|S10", skip_header=1)
symbols = np.genfromtxt("minerals.csv", delimiter=',', usecols=1, dtype="|S10", skip_header=1)
raw_data = np.genfromtxt("minerals.csv", delimiter=',', skip_header=1)[:,2:]
data = {label: row for label, row in zip(labels, raw_data)}

print(data)
