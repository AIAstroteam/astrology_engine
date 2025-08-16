def findAdhiYoga(planetData, includeOuterPlanetsAsMalefics=True, requireMoonWaxing=False, requireMoonInKendra=False):
    """
    Detect Adhi Yoga and its type based on classical conditions.
    Returns a dict with detailed reasoning.
    """

    # Define benefics and malefics
    benefics = ["Jupiter", "Venus", "Mercury"]
    malefics = ["Sun", "Mars", "Saturn", "Rahu", "Ketu"]

    if includeOuterPlanetsAsMalefics:
        malefics.extend(["Uranus", "Neptune", "Pluto"])

    # Check Moon in data
    if "Moon" not in planetData:
        return {"yoga": False, "type": "No Moon data", "notes": "Moon position is required"}

    moon_house = planetData["Moon"]["house"]

    # Determine waxing/waning Moon (needs Sun position)
    moon_waxing = None
    if "Sun" in planetData:
        moon_long = planetData["Moon"]["degree"]
        sun_long = planetData["Sun"]["degree"]
        phase_diff = (moon_long - sun_long) % 360
        moon_waxing = 0 < phase_diff < 180
    else:
        moon_waxing = None  # Can't determine without Sun

    # Houses to check = 6th, 7th, 8th from Moon (inclusive counting)
    houses_from_moon = [((moon_house + i - 1) % 12) + 1 for i in range(5, 8)]

    benefics_found = []
    malefics_found = []
    others_found = []

    # Scan planets in those houses
    for planet, pdata in planetData.items():
        if planet == "Ascendant":
            continue
        if pdata["house"] in houses_from_moon:
            if planet in benefics:
                benefics_found.append(planet)
            elif planet in malefics:
                malefics_found.append(planet)
            else:
                others_found.append(planet)

    # Optional check: require Moon waxing
    if requireMoonWaxing and moon_waxing is not None and not moon_waxing:
        return {
            "yoga": False,
            "type": "Moon is waning",
            "benefics_found": benefics_found,
            "malefics_found": malefics_found,
            "moon_waxing": moon_waxing,
            "moon_house": moon_house,
            "checked_houses_from_moon": houses_from_moon,
            "notes": "Moon is waning — classical Adhi Yoga usually requires waxing Moon"
        }

    # Optional check: require Moon in Kendra from Lagna
    if requireMoonInKendra and "Ascendant" in planetData:
        lagna_house = planetData["Ascendant"]["house"]
        kendras = [lagna_house, ((lagna_house + 3 - 1) % 12) + 1,
                   ((lagna_house + 6 - 1) % 12) + 1, ((lagna_house + 9 - 1) % 12) + 1]
        if moon_house not in kendras:
            return {
                "yoga": False,
                "type": "Moon not in Kendra from Lagna",
                "benefics_found": benefics_found,
                "malefics_found": malefics_found,
                "moon_waxing": moon_waxing,
                "moon_house": moon_house,
                "checked_houses_from_moon": houses_from_moon,
                "notes": "Moon must be in Kendra from Lagna for this stricter definition"
            }

    # Classify yoga type
    if not benefics_found:
        yoga_type = "No Adhi Yoga"
        yoga_present = False
    elif benefics_found and not malefics_found:
        if len(benefics_found) == 3:
            yoga_type = "Full Adhi Yoga"
        elif len(benefics_found) == 2:
            yoga_type = "Medium Adhi Yoga"
        else:
            yoga_type = "Mild Adhi Yoga"
        yoga_present = True
    else:
        yoga_type = "Partial Adhi Yoga (benefics present but malefics also present - spoiled)"
        yoga_present = False  # Classical texts say it's spoiled

    return {
        "yoga": yoga_present,
        "type": yoga_type,
        "benefics_found": benefics_found,
        "malefics_found": malefics_found,
        "other_planets_found": others_found,
        "moon_waxing": moon_waxing,
        "moon_house": moon_house,
        "checked_houses_from_moon": houses_from_moon,
        "notes": f"Benefics in 6/7/8 from Moon: {benefics_found}; "
                 f"Malefics in 6/7/8 from Moon: {malefics_found}; "
                 f"Moon is {'waxing' if moon_waxing else 'waning' if moon_waxing is not None else 'unknown'}"
    }
