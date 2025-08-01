# Need to pass planet_positions as input

# === Example Input ===
planet_positions = {
    "Sun": 323.884958,
    "Moon": 262.812165,
    "Mercury": 301.005367,
    "Venus": 336.694657,
    "Mars": 10.998863,
    "Jupiter": 71.818713,
    "Saturn": 44.900403,
    "Rahu": 58.950951,
    "Ketu": 238.950951,
    "Uranus": 302.233227,
    "Neptune": 285.973825,
    "Pluto": 233.704606
}


# Zodiac signs in order
signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

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

    return signs[d3_index]

# Build D3 chart
def calculate_d3_chart(planet_positions):
    d3_chart = {}
    for planet, degree in planet_positions.items():
        d3_sign = d3_sign_from_d1(degree)
        d3_chart[planet] = d3_sign
    return d3_chart

# Run calculation and print
d3_chart = calculate_d3_chart(planet_positions)

print("📘 D3 (Drekkana) Chart:")
for planet in planet_positions:
    print(f"{planet:<8}: {d3_chart[planet]}")
