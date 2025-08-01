# Need to pass moon_degree, birth_nakshatra and birth_date as input

from datetime import datetime, timedelta
# === Example Usage ===
moon_deg = 262.807670
birth_nakshatra = "Purva Ashadha"
birth_date = datetime(2002, 3, 8)



# Nakshatras in order with their Dasha lords
nakshatras = [
    ("Ashwini", "Ketu"), ("Bharani", "Venus"), ("Krittika", "Sun"), ("Rohini", "Moon"),
    ("Mrigashira", "Mars"), ("Ardra", "Rahu"), ("Punarvasu", "Jupiter"), ("Pushya", "Saturn"),
    ("Ashlesha", "Mercury"), ("Magha", "Ketu"), ("Purva Phalguni", "Venus"), ("Uttara Phalguni", "Sun"),
    ("Hasta", "Moon"), ("Chitra", "Mars"), ("Swati", "Rahu"), ("Vishakha", "Jupiter"),
    ("Anuradha", "Saturn"), ("Jyeshtha", "Mercury"), ("Mula", "Ketu"), ("Purva Ashadha", "Venus"),
    ("Uttara Ashadha", "Sun"), ("Shravana", "Moon"), ("Dhanishta", "Mars"), ("Shatabhisha", "Rahu"),
    ("Purva Bhadrapada", "Jupiter"), ("Uttara Bhadrapada", "Saturn"), ("Revati", "Mercury")
]

# Vimshottari Mahadasha durations in years
dasha_years = {
    "Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10, "Mars": 7,
    "Rahu": 18, "Jupiter": 16, "Saturn": 19, "Mercury": 17
}

def calculate_antardashas(maha_lord, start_date, maha_years):
    """Calculate 9 Antardashas starting from the Mahadasha lord."""
    antardashas = []
    maha_days = maha_years * 365.25
    current_date = start_date

    # Reorder lords to start from the current Mahadasha lord
    lords = list(dasha_years.keys())
    start_index = lords.index(maha_lord)
    ordered_lords = lords[start_index:] + lords[:start_index]

    for sub_lord in ordered_lords:
        proportion = dasha_years[sub_lord] / 120.0
        antar_days = maha_days * proportion
        end_date = current_date + timedelta(days=antar_days)

        antardashas.append({
            "lord": sub_lord,
            "start": current_date,
            "end": end_date
        })

        current_date = end_date

    return antardashas


def calculate_mahadasha_timeline(moon_degree, birth_nakshatra, birth_date):
    degrees_per_nakshatra = 13.333333  # 360 / 27
    nak_index = next(i for i, (name, _) in enumerate(nakshatras) if name == birth_nakshatra)
    start_deg = nak_index * degrees_per_nakshatra
    traversed_deg = moon_degree - start_deg
    percent_used = traversed_deg / degrees_per_nakshatra

    start_dasha_lord = nakshatras[nak_index][1]
    total_years = dasha_years[start_dasha_lord]
    remaining_years = total_years * (1 - percent_used)

    # Generate Mahadasha sequence starting from birth Nakshatra
    sequence = []
    lord_sequence = list(dasha_years.keys())
    start_index = lord_sequence.index(start_dasha_lord)

    current_date = birth_date
    first_end_date = current_date + timedelta(days=remaining_years * 365.25)

    # First Mahadasha with remaining years
    sequence.append({
        "lord": start_dasha_lord,
        "start": current_date,
        "end": first_end_date,
        "antardashas": calculate_antardashas(start_dasha_lord, current_date, remaining_years)
    })

    current_date = first_end_date

    # Add remaining 8 Mahadashas (total 9)
    for i in range(1, 9):
        lord = lord_sequence[(start_index + i) % 9]
        duration = dasha_years[lord]
        end_date = current_date + timedelta(days=duration * 365.25)
        sequence.append({
            "lord": lord,
            "start": current_date,
            "end": end_date,
            "antardashas": calculate_antardashas(lord, current_date, duration)
        })
        current_date = end_date

    return sequence

timeline = calculate_mahadasha_timeline(moon_deg, birth_nakshatra, birth_date)

print(f"🌙 Birth Nakshatra: {birth_nakshatra}")
print(f"🪐 Starting Dasha Lord: {timeline[0]['lord']}")
print("\n🔮 Vimshottari Mahadasha Timeline:")

for maha in timeline:
    print(f"\n🟦 Mahadasha - {maha['lord']}: {maha['start'].date()} → {maha['end'].date()}")
    for antar in maha['antardashas']:
        print(f"   ↳ {antar['lord']}: {antar['start'].date()} → {antar['end'].date()}")
