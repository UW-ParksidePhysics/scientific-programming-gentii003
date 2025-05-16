"""
 for astronomical symbols to be called and a dictionary of planet data

"""
import numpy as np

#This maps planet names to their astronomical symbols
astronomical_symbols = dict(
    Sun='☉',
    Moon='☽',
    Mercury='☿',
    Venus='♀',
    Earth='⊕',
    Mars='♂',
    Jupiter='♃',
    Saturn='♄',
    Uranus='⛢',
    Neptune='♆',
    Pluto='♇',
    Ceres='⚳'
)

# dictionary 
planets_data = {
    'Mercury': {'inclination': 7.0,  't': 0,           'symbol': astronomical_symbols['Mercury'], 'color': 'black'},
    'Venus':   {'inclination': 3.4,  't': np.pi/4,     'symbol': astronomical_symbols['Venus'],   'color': 'black'},
    'Earth':   {'inclination': 0.0,  't': np.pi/2,     'symbol': astronomical_symbols['Earth'],   'color': 'black'},
    'Mars':    {'inclination': 2, 't': np.pi/3,     'symbol': astronomical_symbols['Mars'],    'color': 'black'},
    'Jupiter': {'inclination': 1.3,  't': np.pi/5,     'symbol': astronomical_symbols['Jupiter'], 'color': 'black'},
    'Saturn':  {'inclination': 2.5,  't': np.pi/6,     'symbol': astronomical_symbols['Saturn'],  'color': 'black'},
    'Uranus':  {'inclination': 1,  't': np.pi/8,     'symbol': astronomical_symbols['Uranus'],  'color': 'black'},
    'Neptune': {'inclination': 2,  't': np.pi/9,     'symbol': astronomical_symbols['Neptune'], 'color': 'black'},
    'Ceres':   {'inclination': 11, 't': np.pi/7,     'symbol': astronomical_symbols['Ceres'],   'color': 'black'},
    'Pluto':   {'inclination': 17, 't': np.pi/10,    'symbol': astronomical_symbols['Pluto'], 'color': 'black'},
}