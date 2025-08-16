# Planetary positions in degrees (360° scale)
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

# Zodiac signs (0-based index)
zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# Rulers of the zodiac signs
sign_rulers = {
    "Aries": "Mars",
    "Taurus": "Venus",
    "Gemini": "Mercury",
    "Cancer": "Moon",
    "Leo": "Sun",
    "Virgo": "Mercury",
    "Libra": "Venus",
    "Scorpio": "Mars",
    "Sagittarius": "Jupiter",
    "Capricorn": "Saturn",
    "Aquarius": "Saturn",
    "Pisces": "Jupiter"
}

def get_d60_sign_parashara(degree):
    # Step 1: Get the degree within the sign (0–30°)
    degree_in_sign = degree % 30
    sign_index = int(degree // 30)
    # Step 2: Multiply by 2 and get the integer part
    d60_index = int((degree_in_sign * 2) + sign_index) % 12
    # Step 3: Get the sign and its ruler
    sign = zodiac_signs[d60_index]
    ruler = sign_rulers[sign]
    return sign, ruler

# Compute D60 sign and ruler for all planets
print("🔯 D60 (Shashtiamsa) Chart:")
for planet, deg in planet_positions.items():
    sign, ruler = get_d60_sign_parashara(deg)
    print(f"{planet:<8}: {sign:<10} (Ruler: {ruler})")
