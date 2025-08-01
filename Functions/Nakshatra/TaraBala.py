# Need to pass birth_nakshatra and current_nakshatra as input

# === Example Usage ===
birth_nakshatra = "Purva Ashadha"
current_nakshatra = "Chitra"

import swisseph as swe
from datetime import datetime, timedelta, timezone

# Set path to Swiss Ephemeris data and Lahiri Ayanamsa
swe.set_ephe_path('./ephe/')
swe.set_sid_mode(swe.SIDM_LAHIRI)

# Define IST
IST = timezone(timedelta(hours=5, minutes=30))

# Nakshatra list
nakshatras = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashirsha",
    "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
    "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati",
    "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
    "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

# Tara meaning table
tara_results = {
    1: "Janma (Challenging)",
    2: "Sampat (Good)",
    3: "Vipat (Challenging)",
    4: "Kshema (Very Good)",
    5: "Pratyari (Challenging)",
    6: "Sadhaka (Good)",
    7: "Naidhana (Inauspicious)",
    8: "Mitra (Good)",
    9: "Parama Mitra (Excellent)"
}

# --- Step 1: Input your birth Nakshatra ---

birth_index = nakshatras.index(birth_nakshatra)

# --- Step 2: Get current IST date and Julian Day ---
now_ist = datetime.now(IST)
jd_now = swe.julday(now_ist.year, now_ist.month, now_ist.day,
                    now_ist.hour + now_ist.minute / 60 + now_ist.second / 3600)

# --- Step 3: Get Moon position and current Nakshatra ---
moon_pos, _ = swe.calc(jd_now, swe.MOON)
moon_deg = moon_pos[0]


nakshatra_index = nakshatras.index(current_nakshatra)

# --- Step 4: Calculate Tara Bala position ---
tara_position = ((nakshatra_index - birth_index) % 9) + 1
tara_meaning = tara_results[tara_position]

# --- Output ---
print("🗓️ Current IST Time:", now_ist.strftime("%Y-%m-%d %H:%M:%S"))
print(f"🌙 Current Nakshatra: {current_nakshatra}")
print(f"🧬 Your Birth Nakshatra: {birth_nakshatra}")
print(f"🔮 Tara Bala Result: {tara_meaning}")