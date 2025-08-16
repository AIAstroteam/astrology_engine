# List of zodiac signs in order (0 = Aries, 11 = Pisces)
zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

def get_d12_sign(planet_degree):
    # Step 1: Determine sign index (0 = Aries, ..., 11 = Pisces)
    sign_index = int(planet_degree // 30)
    intra_sign_deg = planet_degree % 30

    # Step 2: Determine D12 division index (each = 2.5°)
    d12_div_index = int(intra_sign_deg // 2.5)

    d12_sign_index = (sign_index + d12_div_index) % 12

    return zodiac_signs[d12_sign_index]

# === Input: Planetary Positions ===
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

# === Compute and Print D12 Signs ===
print("📜 D12 (Dwadashamsha) Signs:")
for planet, degree in planet_positions.items():
    d12_sign = get_d12_sign(degree)
    print(f"{planet}: D12 sign = {d12_sign}")
