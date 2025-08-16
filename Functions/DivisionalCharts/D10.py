# List of zodiac signs in order
zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

def get_d10_sign(planet_degree):
    # 1. Determine sign index (0 = Aries)
    sign_index = int(planet_degree // 30)
    sign_name = zodiac_signs[sign_index]

    # 2. Degree within the sign
    intra_sign_deg = planet_degree % 30

    # 3. Each D10 division = 3°
    division_index = int(intra_sign_deg // 3)

    if sign_index % 2 == 0:
        # Odd sign: count from same sign
        d10_sign_index = (sign_index + division_index) % 12
    else:
        # Even sign: count from 9th sign from it (i.e., +8)
        d10_sign_index = (sign_index + 8 + division_index) % 12

    return zodiac_signs[d10_sign_index]

# === Input: Planetary Positions in Degrees ===
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

# === Calculate and Print D10 Signs ===
d10_signs = {planet: get_d10_sign(degree) for planet, degree in planet_positions.items()}

for planet, sign in d10_signs.items():
    print(f"{planet}: D10 sign = {sign}")
