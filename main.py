# To be written
import swisseph as swe
import Functions.LagnaAndPlanetData.PlanetData as pd
import Functions.Nakshatra.BirthNakshatra as bn

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
# print("Lagna:", lagnaName)
# print("\nPlanet Positions:")
# for planet, data in planetHouses.items():
#     print(f"{planet}: {data['house']}, {data['degree']}, {data['sign']}")


moonDegrees = planetHouses["Moon"]["degree"]
birthNakshatra = bn.getBirthNakshatra(moonDegrees)
# print(f"🌙 Moon Nakshatra: {birthNakshatra['nakshatra']}")
# print(f"📍 Pada: {birthNakshatra['pada']}")
# print(f"🪐 Dasha Lord: {birthNakshatra['rulingPlanet']}")

