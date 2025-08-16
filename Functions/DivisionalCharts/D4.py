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

def get_d4_sign(degree):
    sign_index = int(degree // 30)
    deg_in_sign = degree % 30
    division_index = int(deg_in_sign // 7.5)  # Each quarter is 7.5°

    if division_index == 0:
        base_sign = (sign_index + 0) % 12
    elif division_index == 1:
        base_sign = (sign_index + 3) % 12
    elif division_index == 2:
        base_sign = (sign_index + 6)% 12
    elif division_index == 3:
        base_sign = (sign_index + 9)% 12

    return signs[base_sign]

# Build D4 Chart
d4_chart = {}
for planet, deg in planet_positions.items():
    d4_chart[planet] = get_d4_sign(deg)

# Display result
print("🪐 Corrected D4 (Chaturthamsha) Chart:")
for planet, sign in d4_chart.items():
    print(f"{planet}: {sign}")
