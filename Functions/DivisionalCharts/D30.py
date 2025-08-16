signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

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
    "Ascendant": 123.456
}

# Ruler → sign mapping based on odd/even signs
ruler_to_sign_map = {
    "Mars":     {"odd": "Aries",       "even": "Scorpio"},
    "Venus":    {"odd": "Libra",       "even": "Taurus"},
    "Mercury":  {"odd": "Gemini",      "even": "Virgo"},
    "Jupiter":  {"odd": "Sagittarius", "even": "Pisces"},
    "Saturn":   {"odd": "Aquarius",    "even": "Capricorn"}
}

def get_d30_ruler_and_sign(degree):
    sign_index = int(degree // 30)
    degree_in_sign = degree % 30
    is_odd_sign = sign_index % 2 == 0  # 0=Aries, 2=Gemini, etc.
    
    if is_odd_sign:
        if 0 <= degree_in_sign < 5:
            ruler = "Mars"
        elif 5 <= degree_in_sign < 10:
            ruler = "Saturn"
        elif 10 <= degree_in_sign < 18:
            ruler = "Jupiter"
        elif 18 <= degree_in_sign < 25:
            ruler = "Mercury"
        elif 25 <= degree_in_sign <= 30:
            ruler = "Venus"
    else:
        if 0 <= degree_in_sign < 5:
            ruler = "Venus"
        elif 5 <= degree_in_sign < 12:
            ruler = "Mercury"
        elif 12 <= degree_in_sign < 20:
            ruler = "Jupiter"
        elif 20 <= degree_in_sign < 25:
            ruler = "Saturn"
        elif 25 <= degree_in_sign <= 30:
            ruler = "Mars"

    # Get corresponding sign based on odd/even nature
    d30_sign = ruler_to_sign_map[ruler]["odd" if is_odd_sign else "even"]
    return ruler, d30_sign

# ---- Output ----
print("🌗 D30 Trimshamsha Chart (Ruler + Correct Sign):")
print(f"{'Body':>12} | {'Ruler':<8} | {'D30 Sign':<10}")
print("-" * 35)

for body, degree in planet_positions.items():
    ruler, d30_sign = get_d30_ruler_and_sign(degree)
    print(f"{body:>12} | {ruler:<8} | {d30_sign:<10}")
