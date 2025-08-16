def get_d20_sign(degree):
    # Zodiac signs in order
    signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]

    # Sign types by index: 0=Aries, ..., 11=Pisces
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

    # Step 1: Determine Rashi and position in sign
    sign_index = int(degree // 30)
    degree_in_sign = degree % 30

    # Step 2: Determine Vimshamsha (D20) division (each = 1.5°)
    d20_div_index = int(degree_in_sign // 1.5)  # 0-based index (0 to 19)

    # Step 3: Starting sign based on sign type
    sign_type = sign_types[sign_index]
    if sign_type == "Movable":
        start_index = 0
    elif sign_type == "Fixed":
        start_index = 8  # 9th from current
    elif sign_type == "Dual":
        start_index = 4 # 5th from current
    else:
        raise ValueError("Invalid sign type.")

    # Step 4: Final D20 sign = start + division offset
    d20_sign_index = (start_index + d20_div_index) % 12
    d20_sign_name = signs[d20_sign_index]

    return {
        "degree": degree,
        "rashi": signs[sign_index],
        "sign_type": sign_type,
        "d20_division": d20_div_index + 1,
        "d20_sign": d20_sign_name
    }

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

for planet, degree in planet_positions.items():
    result = get_d20_sign(degree)
    print(f"{planet}: {result['d20_sign']} (D20 Division {result['d20_division']}, Base: {result['rashi']} - {result['sign_type']})")