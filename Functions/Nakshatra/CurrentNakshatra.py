import swisseph as swe
import datetime

# Set ephemeris path (make sure you downloaded and extracted Swiss Ephemeris files here)
swe.set_ephe_path('./ephe/')
swe.set_sid_mode(swe.SIDM_LAHIRI)  # Use Lahiri Ayanamsa

# --- Current datetime in IST (UTC+5:30) ---
now_ist = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))

# Convert IST to UTC for Swiss Ephemeris
now_utc = now_ist.astimezone(datetime.timezone.utc)

# Calculate Julian Day in UT
jd_ut = swe.julday(now_utc.year, now_utc.month, now_utc.day,
                   now_utc.hour + now_utc.minute / 60 + now_utc.second / 3600)

# Get Moon's sidereal position
moon_pos, _ = swe.calc_ut(jd_ut, swe.MOON)
ayanamsa = swe.get_ayanamsa(jd_ut)
moon_sidereal = moon_pos[0] - ayanamsa
if moon_sidereal < 0:
    moon_sidereal += 360

# Nakshatra list
nakshatras = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta",
    "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

# Each Nakshatra is 13°20' = 13.333... degrees
nakshatra_index = int(moon_sidereal // (360 / 27))
nakshatra = nakshatras[nakshatra_index]

# Pada calculation (each Nakshatra has 4 padas of 3°20')
pada = int((moon_sidereal % (360 / 27)) // (360 / 108)) + 1

# Output
print(f"🗓️ Current IST Time: {now_ist.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"🌙 Moon Sidereal Longitude: {moon_sidereal:.6f}°")
print(f"✨ Current Nakshatra: {nakshatra}")
print(f"📍 Pada: {pada}")
