# To be written
import swisseph as swe
import utils.constants as const
import Functions.LagnaAndPlanetData.PlanetData as pd
import Functions.Nakshatra.BirthNakshatra as bn
import Functions.Yoga.YogaCalculations as yc
import Functions.Yoga.RajYoga as ry
import Functions.Yoga.DhanaYoga as dy 
import Functions.Yoga.VipritaRajYoga as vrp
import Functions.Yoga.GajaKesariYoga as gky
import Functions.Yoga.ChandraMangalYoga as cmy
import Functions.Yoga.AdhiYoga as ay
import Functions.Yoga.LakshmiYoga as ly

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

lagnaSignIndex, planetHouses = pd.getLagnaAndPlanetHouses(julianDay, latitude, longitude)
# print("Lagna:", lagnaName)
# print("\nPlanet Positions:")
# for planet, data in planetHouses.items():
#     print(f"{planet}: {data['house']}, {data['degree']}, {data['sign']}")
print(planetHouses)


moonDegrees = planetHouses["Moon"]["degree"]
birthNakshatra = bn.getBirthNakshatra(moonDegrees)
# print(f"🌙 Moon Nakshatra: {birthNakshatra['nakshatra']}")
# print(f"📍 Pada: {birthNakshatra['pada']}")
# print(f"🪐 Dasha Lord: {birthNakshatra['rulingPlanet']}")

yoga = yc.detectMahaPurushaYogas(planetHouses)
# print(yoga)

rajYoga = ry.findRajaYogas(planetHouses, const.signLords)
#print(rajYoga)

dhanyoga = dy.findDhanaYogas(planetHouses, const.signLords)
#print(dhanyoga)

vipritaRajYoga = vrp.findViparitaRajaYogas(planetHouses, const.signLords)
#print(vipritaRajYoga)

gajaKesariYog = gky.findGajaKesariYoga(planetHouses)
#print(gajaKesariYog)

chandraMangalYoga = cmy.findChandraMangalaYoga(planetHouses,lagnaSignIndex)
#print(chandraMangalYoga)

adhiYoga = ay.findAdhiYoga(planetHouses, False, True, False)
#print(adhiYoga)

lakshmiYoga = ly.findLakshmiYoga(planetHouses, lagnaSignIndex + 1)
print(lakshmiYoga)