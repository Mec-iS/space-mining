# All masses are in kilograms
import pandas as pd
import numpy as np

#
# Base data
#
total_mass_sun = 1.989 * 1e30                   # total mass of the Sun
total_mass_of_ss = total_mass_sun * 1.0014      # total mass of the S.S.: 1.991784 e+30
total_mass_non_sun = total_mass_of_ss - total_mass_sun   # the mass of the rest of the system is 0,14% of the total
print(total_mass_non_sun)

total_mass_of_terrestrial = 1.18 * 1e25
total_mass_of_gas_planets =  2.26 * 1e27
total_mass_of_minor_bodies = 4.282 * 1e26

total_non_sun = total_mass_of_terrestrial + total_mass_of_gas_planets + total_mass_of_minor_bodies
total_dust_and_other = total_mass_non_sun - total_non_sun   # moons, asteroids, comets
print(total_dust_and_other)


earth_mass = 5.972 * 1e24
earth_crust_mass = 0.026 * 1e24
crust_over_mass_ratio = earth_crust_mass / earth_mass
#print('Percentage of crust over total mass: % ', mass_crust_ratio)

#
# optimistically consider that we can mine 30% of the crust of a planet's crust
#
crust_reachable = 0.3 * crust_over_mass_ratio
#print('Percentage of a terretrial planet minable: %', crust_reachable)

#
# total minable in terrestrial planets (excluding Earth)
#
total_minable_in_terrestrial = (total_mass_of_terrestrial - earth_mass) * crust_reachable
print('Total mass minable in terrestrial planets: Kg ', total_minable_in_terrestrial)

#
# optimistically consider that we can mine 10% of a minor planet
#
minor_planets_minable_esteem =  0.1
total_mass_minor_planets = earth_mass / 847   # first 1549 minor planets
total_mass_minable_minor_planets = total_mass_minor_planets * minor_planets_minable_esteem
print('Minable mass of minor planets: Kg ', total_mass_minable_minor_planets)

#
# optimistically consider that we can mine 90% of a small body
#
small_bodies_minable_esteem = 0.9
total_mass_small_bodies = total_mass_of_minor_bodies - total_mass_minor_planets
total_mass_minable_small_bodies = total_mass_small_bodies * small_bodies_minable_esteem
print('Minable mass of small bodies: Kg ', total_mass_minable_small_bodies)


from pprint import pprint as pp

labels = np.genfromtxt("minerals.csv", delimiter=',', usecols=0, dtype="|S10", skip_header=1)
symbols = np.genfromtxt("minerals.csv", delimiter=',', usecols=1, dtype="|S10", skip_header=1)
raw_data = np.genfromtxt("minerals.csv", delimiter=',', skip_header=1)[:,2:]
data = {label: row for label, row in zip(symbols, raw_data)}

pp(data)