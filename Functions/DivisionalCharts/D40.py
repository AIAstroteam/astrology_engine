# Define the 12 zodiac signs in order
signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# Signs considered odd (count from Aries), even (count from Libra)
odd_signs = [0, 2, 4, 6, 8, 10]  # Aries, Gemini, Leo, Libra, Sagittarius, Aquarius
even_signs = [1, 3, 5, 7, 9, 11] # Taurus, Cancer, Virgo, Scorpio, Capricorn, Pisces

def get_d40_sign(degree):
    sign_index = int(degree // 30)
    degree_in_sign = degree % 30
    part_index = int(degree_in_sign // 0.75)  # D40 = 0.75° = 45'

    if sign_index in odd_signs:
        base = 0  # Aries
    else:
        base = 6  # Libra

    d40_index = (base + part_index) % 12
    return signs[d40_index]

# Example for all planets
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
    "Pluto": 233.704606,
    "Ascendant": 140.49
}

print("🌗 D40 (Khavedamsha) Signs:")
for planet, deg in planet_positions.items():
    d40_sign = get_d40_sign(deg)
    print(f"{planet:>10}: {d40_sign}")
