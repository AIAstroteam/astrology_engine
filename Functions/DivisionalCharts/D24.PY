def get_d24_sign(degree):
    # Zodiac signs
    signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]

    # Step 1: Get base sign
    sign_index = int(degree // 30)
    sign_name = signs[sign_index]
    degree_in_sign = degree % 30

    # Step 2: D24 division (each = 1.25°)
    d24_div_index = int(degree_in_sign // 1.25)  # 0-based index (0 to 23)

    # Step 3: Determine direction based on odd/even
    if sign_index % 2 == 0:
        d24_sign_index = (4 + d24_div_index) % 12
    else:
        d24_sign_index = (3 + d24_div_index) % 12

    d24_sign = signs[d24_sign_index]

    return {
        "degree": degree,
        "rashi": sign_name,
        "even_or_odd": "Odd" if sign_index % 2 == 0 else "Even",
        "d24_division": d24_div_index + 1,
        "d24_sign": d24_sign
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

print("🪐 D24 Siddhamsha Signs (Old Even/Odd Logic):")
for planet, degree in planet_positions.items():
    result = get_d24_sign(degree)
    print(f"{planet:<8}: {result['d24_sign']:>9} (Div {result['d24_division']:>2}, Base: {result['rashi']} - {result['even_or_odd']})")
