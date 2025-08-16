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

signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

def get_d27_sign_with_if_else(degree):
    sign_index = int(degree // 30)
    degree_in_sign = degree % 30
    division_size = 30 / 27  # ≈ 1.111111°
    division_index = int(degree_in_sign // division_size)

    # Determine the starting sign based on element
    if sign_index in [0, 4, 8]:  # Fire: Aries, Leo, Sagittarius
        start_index = 0  # Aries
    elif sign_index in [1, 5, 9]:  # Earth: Taurus, Virgo, Capricorn
        start_index = 3  # Cancer
    elif sign_index in [2, 6, 10]:  # Air: Gemini, Libra, Aquarius
        start_index = 6  # Libra
    elif sign_index in [3, 7, 11]:  # Water: Cancer, Scorpio, Pisces
        start_index = 9  # Capricorn
    else:
        start_index = 0  # Fallback to Aries (should not occur)

    d27_index = (start_index + division_index) % 12
    return signs[d27_index]

# ---- Compute and print results ----
print("🌗 D27 Bhamsa Signs (Element-Based Logic with if-else):")
for planet, degree in planet_positions.items():
    d27_sign = get_d27_sign_with_if_else(degree)
    print(f"{planet:>8}: {d27_sign}")
