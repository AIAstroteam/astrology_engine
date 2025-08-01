import swisseph as swe
import datetime

# Set ephemeris path and sidereal mode
swe.set_ephe_path('./ephe/')
swe.set_sid_mode(swe.SIDM_LAHIRI)

# Zodiac signs
zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# 1. Define birth date/time in IST
birth_dt_ist = datetime.datetime(2002, 3, 8, 18, 20)

# 2. Convert IST to UTC
birth_dt_utc = birth_dt_ist - datetime.timedelta(hours=5, minutes=30)

# 3. Calculate Julian Day (UT)
jd_ut = swe.julday(
    birth_dt_utc.year, birth_dt_utc.month, birth_dt_utc.day,
    birth_dt_utc.hour + birth_dt_utc.minute / 60.0
)

# 4. Tropical positions
sun_trop, _ = swe.calc_ut(jd_ut, swe.SUN)
moon_trop, _ = swe.calc_ut(jd_ut, swe.MOON)

sun_sign_tropical = zodiac_signs[int(sun_trop[0] // 30)]
moon_sign_tropical = zodiac_signs[int(moon_trop[0] // 30)]

# 5. Get Ayanamsa and calculate sidereal positions
ayanamsa = swe.get_ayanamsa(jd_ut)

# Sidereal Sun and Moon (subtract ayanamsa and normalize if < 0)
sun_sidereal = sun_trop[0] - ayanamsa
moon_sidereal = moon_trop[0] - ayanamsa

if sun_sidereal < 0:
    sun_sidereal += 360
if moon_sidereal < 0:
    moon_sidereal += 360

sun_sign_sidereal = zodiac_signs[int(sun_sidereal // 30)]
moon_sign_sidereal = zodiac_signs[int(moon_sidereal // 30)]

# 6. Print results
print("🧭 Tropical (Western) Zodiac:")
print(f"   Sun Sign:  {sun_sign_tropical} ({sun_trop[0]:.6f}°)")
print(f"   Moon Sign: {moon_sign_tropical} ({moon_trop[0]:.6f}°)\n")

print("🪔 Sidereal (Vedic) Zodiac (Lahiri Ayanamsa):")
print(f"   Sun Sign:  {sun_sign_sidereal} ({sun_sidereal:.6f}°)")
print(f"   Moon Sign: {moon_sign_sidereal} ({moon_sidereal:.6f}°)")
