
from utils import constants as const
from utils import helpers
# === Example Input ===

# Function to get D2 (Hora) sign
def get_d2_hora_sign(longitude_deg):
    sign_index = int(longitude_deg // 30)
    degree_in_sign = longitude_deg % 30

    if sign_index in const.oldSigns:
        if degree_in_sign < 15:
            return "Leo"   # Sun's Hora
        else:
            return "Cancer"  # Moon's Hora
    else:
        if degree_in_sign < 15:
            return "Cancer"  # Moon's Hora
        else:
            return "Leo"   # Sun's Hora


def get_d9_navamsa(planet_signs):
    d9_chart = {}
    for planet, (sign, deg_in_sign) in planet_signs.items():
        navamsa_num = int(deg_in_sign // (30 / 9)) + 1  # 1 to 9
        sign_index =  const.zodiacSigns.index(sign)
        sign_type = const.signType[sign]

        if sign_type == "Movable":
            d9_index = (sign_index + (navamsa_num - 1)) % 12
        elif sign_type == "Fixed":
            # Reverse count from the 9th sign from Rasi
            start_index = (sign_index + 8) % 12
            d9_index = (start_index + (navamsa_num - 1)) % 12
        elif sign_type == "Dual":
            d9_index = (sign_index + 4 + (navamsa_num - 1)) % 12

        d9_sign = const.zodiacSigns[d9_index]
        d9_chart[planet] = d9_sign
    return d9_chart

d2_chart = {}
for planet, pos in helpers.extractPlanetDegree.items():
    d2_chart[planet] = get_d2_hora_sign(pos)

# Print the D2 (Hora) chart
print("📜 D2 (Hora) Chart:")
for planet, hora_sign in d2_chart.items():
    print(f"{planet:8} → {hora_sign}")

# Step 1: Get (sign, degree in sign)
planet_signs = helpers.reverse_reference_degrees(helpers.extractPlanetDegree())

# Step 2: Compute D9 Navamsa chart
d9_result = get_d9_navamsa(planet_signs)

# Step 3: Print D9 Chart
print("🧭 D9 Navamsa Chart:")
for planet, d9_sign in d9_result.items():
    print(f"{planet}: {d9_sign}")
