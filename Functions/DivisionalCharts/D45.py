planet_positions = {
    "Sun": 323.884958,
    "Moon": 262.812165,
    "Mercury": 301.005367,
    "Venus": 336.694657,
    "Mars": 10.998863,
    "Jupiter": 71.818713,
    "Saturn": 44.900403,
    "Rahu": 58.950951,
    "Ketu": 238.950951
}

zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# Sign classification
sign_nature = {
    "Aries": "movable", "Taurus": "fixed", "Gemini": "dual", "Cancer": "movable",
    "Leo": "fixed", "Virgo": "dual", "Libra": "movable", "Scorpio": "fixed",
    "Sagittarius": "dual", "Capricorn": "movable", "Aquarius": "fixed", "Pisces": "dual"
}
sign_lords = {
    "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
    "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
    "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
}
# Starting sign for counting based on nature
start_sign_map = {
    "movable": "Aries",
    "fixed": "Leo",
    "dual": "Sagittarius"
}

def get_d45_sign(planet_degree):
    degree_in_sign = degree % 30
    aksha = int(degree_in_sign / (30 / 45)) + 1  # Akshavedamsa number 1-540
    sign_index = int(planet_degree // 30)        # 0-based sign index
    sign = zodiac_signs[sign_index]
    sign_type = sign_nature[sign]
    start_sign = start_sign_map[sign_type]
    start_index = zodiac_signs.index(start_sign)

    d45_index = (start_index + aksha) % 12
    d45_sign = zodiac_signs[d45_index -1]
    d45_lord = sign_lords[d45_sign]
    return d45_sign, d45_lord

# Compute for all planets
for planet, degree in planet_positions.items():
    d45_sign, d45_lord = get_d45_sign(degree)
    print(f"{planet}: {d45_sign} , Lord: {d45_lord}")