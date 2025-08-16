# Need to pass planet_positions as input

from utils import constants as const

# Get Rasi (sign) index from full degree (0–360°)
def get_sign_index(degree):
    return int(degree // 30)

# Get degree within the sign (0–30°)
def get_deg_in_sign(degree):
    return degree % 30

# Compute D3 sign based on D1 degree using Vedic Drekkana rules
def d3_sign_from_d1(degree):
    rasi_index = get_sign_index(degree)
    deg_in_sign = get_deg_in_sign(degree)

    if deg_in_sign < 10:
      d3_index = rasi_index
    elif deg_in_sign < 20:
      d3_index = (rasi_index + 4) % 12  # 5th
    else:
     d3_index = (rasi_index + 8) % 12  # 9th

    return const.zodiacSigns[d3_index]

# Build D3 chart
def calculate_d3_chart(planet_positions):
    d3_chart = {}
    for planet, degree in planet_positions.items():
        d3_sign = d3_sign_from_d1(degree)
        d3_chart[planet] = d3_sign
    return d3_chart

