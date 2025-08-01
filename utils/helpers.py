"""
Helper functions for astrological calculations
"""

import math
from datetime import datetime, timedelta
from utils import constants as const

def extractPlanetDegree(planetHouses):
    """
    Args:
        planetHouses (dict): {
            "Sun": {"house": 7, "degree": 336.694657},
            ...
        }

    Returns:
        dict: {
            "Sun": 7,
            ...
        }
    """
    return {planet: data["degree"] for planet, data in planetHouses.items()}

def reverse_reference_degrees(ref_degrees):
    planet_signs = {}
    for planet, absolute_deg in ref_degrees.items():
        sign_index = int(absolute_deg // 30)
        degree_in_sign = round(absolute_deg % 30, 6)
        sign = const.zodiacSigns[sign_index % 12]
        planet_signs[planet] = (sign, degree_in_sign)
    return planet_signs
