# List of zodiac signs
zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

def get_d7_sign(planet_degree):
    sign_index = int(planet_degree // 30)
    intra_sign_deg = planet_degree % 30
    part_size = 30 / 7
    d7_index = int(intra_sign_deg // part_size)
    print(sign_index)
    if sign_index % 2 == 0:  # Odd sign
        d7_sign_index = (sign_index + d7_index) % 12
    else:  # Even sign
        d7_sign_index = (sign_index + 6 + d7_index) % 12

    return zodiac_signs[d7_sign_index]

# Dictionary of planet positions
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

# Compute and print D7 signs
d7_signs = {planet: get_d7_sign(degree) for planet, degree in planet_positions.items()}

for planet, d7 in d7_signs.items():
    print(f"{planet}: D7 sign = {d7}")
