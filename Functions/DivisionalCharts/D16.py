def get_d16_sign(degree):
    signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]

    sign_types = {
        0: "Movable",   # Aries
        1: "Fixed",     # Taurus
        2: "Dual",      # Gemini
        3: "Movable",   # Cancer
        4: "Fixed",     # Leo
        5: "Dual",      # Virgo
        6: "Movable",   # Libra
        7: "Fixed",     # Scorpio
        8: "Dual",      # Sagittarius
        9: "Movable",   # Capricorn
        10: "Fixed",    # Aquarius
        11: "Dual"      # Pisces
    }

    sign_index = int(degree // 30)
    degree_in_sign = degree % 30
    d16_division_index = int(degree_in_sign // 1.875)
    sign_type = sign_types[sign_index]

    if sign_type == "Movable":
        start_index = 0
    elif sign_type == "Fixed":
        start_index = 4
    elif sign_type == "Dual":
        start_index = 8 
    else:
        raise ValueError("Unknown sign type")

    d16_sign_index = (start_index + d16_division_index) % 12
    return signs[d16_sign_index]

# Input planetary positions
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

# Calculate and display D16 signs
d16_chart = {}
for planet, degree in planet_positions.items():
    d16_sign = get_d16_sign(degree)
    d16_chart[planet] = d16_sign

# Output the full D16 chart
for planet, sign in d16_chart.items():
    print(f"{planet}: {sign}")
