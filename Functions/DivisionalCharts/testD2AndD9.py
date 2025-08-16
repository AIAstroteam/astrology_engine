
import Functions.DivisionalCharts.D2andD9 as d2
import swisseph as swe
import Functions.LagnaAndPlanetData.PlanetData as pd
import Functions.Nakshatra.BirthNakshatra as bn
import utils.helpers as helpers
import Functions.DivisionalCharts.D3 as d3

# --- Input ---
dob = "2002-03-08"
time = "18:20"
timezone = 5.5  # IST
latitude = 29.903839
longitude = 73.877190

# --- Parse and convert time to UTC ---
year, month, day = map(int, dob.split("-"))
hour, minute = map(int, time.split(":"))
decimal_time = hour + minute / 60
utc_time = decimal_time - timezone

# --- Julian Day ---
julianDay = swe.julday(year, month, day, utc_time)

lagnaName, planetHouses = pd.getLagnaAndPlanetHouses(julianDay, latitude, longitude)

planetPositions = helpers.extractPlanetDegree(planetHouses);

d2_chart = {}
for planet, pos in planetPositions.items():
    d2_chart[planet] = d2.get_d2_hora_sign(pos)

# Print the D2 (Hora) chart
print("📜 D2 (Hora) Chart:")
for planet, hora_sign in d2_chart.items():
    print(f"{planet:8} → {hora_sign}")

# Step 1: Get (sign, degree in sign)
planet_signs = helpers.reverse_reference_degrees(planetPositions)

# Step 2: Compute D9 Navamsa chart
d9_result = d2.get_d9_navamsa(planet_signs)

# Step 3: Print D9 Chart
print("🧭 D9 Navamsa Chart:")
for planet, d9_sign in d9_result.items():
    print(f"{planet}: {d9_sign}")
