import math

def molar_concentration(relative_humidity, pressure, temp_kelvin):
    psat_over_pr = 10**(-6.8346*((273.16/temp_kelvin)**1.261) + 4.6151)
    molar_concentration = (relative_humidity*(psat_over_pr))/(pressure/101.325)
    return molar_concentration

def oxygen_relaxation_frequency(molar_concentration, pressure):
    relaxation_freq = (pressure/101.325)*(24 + 4.04*(10**4)*molar_concentration*((0.02+molar_concentration)/(0.391+molar_concentration)))
    return relaxation_freq

def nitrogen_relaxation_frequency(molar_concentration, pressure, temp_kelvin):
    relaxation_freq = (pressure/101.325)*((temp_kelvin/293.15)**-0.5)*(9 + 280 * molar_concentration * math.exp(-4.170*(((temp_kelvin/293.15)**(-1/3))- 1)))
    return relaxation_freq

def alphas(fr0, frN, pa, t, list): #Function to find alpha for 9613-1
  for i in range(-13, 8):
    fm2 = ((1000*((10**0.1)**i))**2)
    pa_over_pr = pa/101.325
    t_over_t0 = t / 293.15
    exp1 = (math.exp(-2239.1/t))
    exp2 = (math.exp(-3352/t))
    frequation = ((fr0 + (fm2/fr0))**-1)
    fnequation = ((frN + (fm2/frN))**-1)

    coefficient = 8.686*fm2*((1.84*(10**-11)*(pa_over_pr**-1)*(t_over_t0**0.5))+(t_over_t0**-2.5)*(0.01275*exp1*frequation + 0.1068*exp2*fnequation))
    list.append(coefficient)

def m_values(alpha_list, m_list): #function to calculate m for each frequency, from values of alpha
  for num in alpha_list:
    m_value = num / (10 * math.log10(math.e))
    m_list.append(m_value)

def equivalent_sound_absorption_area_test_specimen(rev_times_empty, rev_times_specimen, m_values_empty, m_values_speicmen, temp_degrees_empty, temp_degrees_specimen, list_of_Absoprtion_areas):
  speed_of_sound_empty = 331 + 0.6*temp_degrees_empty
  speed_of_sound_specimen = 331 + 0.6*temp_degrees_specimen
  i = 0
  while i < len(rev_times_empty):
    absorption_area = 55.3 * room_volume * ((1/(speed_of_sound_specimen*rev_times_specimen[i])) - (1/(speed_of_sound_empty*rev_times_empty[i]))) - 4 * room_volume * (m_values_speicmen[i] - m_values_empty[i]) 
    i += 1
    list_of_Absoprtion_areas.append(absorption_area)

def sound_absorption_coefficient(test_specimen_absorption_areas, specimen_area, list_for_absorption_coefficients):
  for num in test_specimen_absorption_areas:
      absorption_coefficient = num / specimen_area
      list_for_absorption_coefficients.append(absorption_coefficient)

#variables required for manual input are set here, enter room conditions, frequency range, and rev times recorded
room_volume = 196
specimen_area = 10.8
empty_temp = 19.60
empty_temp_kelvin = empty_temp + 273.15
empty_humidity = 67.90
empty_pressure = 101.53
specimen_temp = 19.90
specimen_temp_kelvin = specimen_temp + 273.15
specimen_humidity = 66.30
specimen_pressure = 101.46
frequencies = [50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000]
rev_times_empty = [26.66, 19.09, 15.83, 15.75, 12.40, 9.09, 8.71, 9.58, 9.96, 10.15, 9.10, 8.96, 8.58, 8.18, 7.22, 6.21, 5.45, 4.95, 4.21, 3.51, 2.66]
rev_times_specimen = [10.87, 5.17, 5.80, 5.28, 4.75, 3.87, 3.20, 2.95, 2.84, 2.82, 2.60, 2.75, 2.96, 3.15, 2.92, 2.84, 2.79, 2.62, 2.43, 2.22, 1.90]

# calculating h, the molar concentration of water vapour in the room for each room condition
try:
  molar_concentration_empty = molar_concentration(empty_humidity, empty_pressure, empty_temp_kelvin)
  print("Value of molar concentration in empty room:")
  print(molar_concentration_empty)
  print("\n")
except:
  print("Error calling molar concentration function for empty room")

try:
  molar_concentration_specimen = molar_concentration(specimen_humidity, specimen_pressure ,specimen_temp_kelvin)
  print("Value of molar concentration in room with specimen:")
  print(molar_concentration_empty)
  print("\n")
except:
  print("Error calling molar concentration function for room with specimen") 


# calculating the relaxation frequencies for oxygen and nitrogen in the room conditions
try:
  empty_oxygen_relaxation_frequency = oxygen_relaxation_frequency(molar_concentration_empty, empty_pressure)
  specimen_oxygen_relaxation_frequency = oxygen_relaxation_frequency(molar_concentration_specimen, specimen_pressure)
  print("Value of empty room oxygen relaxation frequency:")
  print(empty_oxygen_relaxation_frequency)
  print("\n")
  print("Value of room with specimen oxygen relaxation frequency:")
  print(specimen_oxygen_relaxation_frequency)
  print("\n")
except:
  print("Error calling the oxygen relaxation frequency functions")
 
try: 
  empty_nitrogen_relaxation_frequency = nitrogen_relaxation_frequency(molar_concentration_empty, empty_pressure, empty_temp_kelvin)
  print("value of empty room nitrogen relaxation frequency:")
  print(empty_nitrogen_relaxation_frequency)
  print("\n")
  specimen_nitrogen_relaxation_frequency = nitrogen_relaxation_frequency(molar_concentration_specimen, specimen_pressure, specimen_temp_kelvin)
  print("Value of room with specimen nitrogen relaxation frequency:")
  print(specimen_nitrogen_relaxation_frequency)
  print("\n")
except:
  print("Error calling the nitrogen relaxation frequency functions")

# calculating and adding the attenuation coefficients (alpha) to a list for the empty room and room with the specimen in
alpha_empty = []
alpha_specimen = []
try:
  alphas(empty_oxygen_relaxation_frequency, empty_nitrogen_relaxation_frequency, empty_pressure, empty_temp_kelvin, alpha_empty)
  print("Alpha values for the empty room:")
  print(alpha_empty)
  print("\n")
  alphas(specimen_oxygen_relaxation_frequency, specimen_nitrogen_relaxation_frequency, specimen_pressure, specimen_temp_kelvin, alpha_specimen)
  print("Alpha values for the room with the specimen:")
  print(alpha_specimen)
  print("\n")
except:
  print("Error occured when calling alphas function")

# Calculation power attenuation coefficients (m) for both room conditions and storing to lists for empty and room with specimen in
m_empty = []
m_specimen = []
try:
  print("List of m_values, first empty, then with specimen:")
  m_values(alpha_empty, m_empty)
  m_values(alpha_specimen, m_specimen)
  print("power attenuation coefficients (m) for empty room:")
  print(m_empty)
  print("\n")
  print("Power attenuation coefficients (m) for the room with the specimen:")
  print(m_specimen)
  print("\n")
except:
  print("Error occured when calling power attenuation coefficent function")

# Calculation the absorption areas for the test specimen amnd storing to a list 
absorption_areas_test_specimen = []
try:
  equivalent_sound_absorption_area_test_specimen(rev_times_empty, rev_times_specimen, m_empty, m_specimen, empty_temp, specimen_temp, absorption_areas_test_specimen)
  print("Eqvuivalent sound absorption areas of test specimen:")
  print(absorption_areas_test_specimen)
  print("\n")
except:
  print("Error occured when calling equivalent sound absorption area test specimen function")

# Calculating the absorption coefficients of the test specimen, and storing to a list
absorption_coefficients = []
try:
  sound_absorption_coefficient(absorption_areas_test_specimen, specimen_area, absorption_coefficients)
except:
  print("Error occured when calling sound_absorption_coefficient function")


# Creating a dictionary of key = frequency and value = absorption coefficient, with values rounded to 2 decimal places
rounded_absorption_coefficients = [round(num, 2) for num in absorption_coefficients]
try:
  frequency_and_values = dict(zip(frequencies, rounded_absorption_coefficients))
  print("Values of absorption coefficients to frequencies")
  print(frequency_and_values)
except:
  print("Error rounding coefficients or in dictionary creation")