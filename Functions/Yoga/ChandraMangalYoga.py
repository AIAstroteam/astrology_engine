def findChandraMangalaYoga(planetData, lagnaSignIndex):
    # Sign lord mapping (sidereal Vedic)
    sign_lords = {
        1: "Mars",    # Aries
        2: "Venus",   # Taurus
        3: "Mercury", # Gemini
        4: "Moon",    # Cancer
        5: "Sun",     # Leo
        6: "Mercury", # Virgo
        7: "Venus",   # Libra
        8: "Mars",    # Scorpio
        9: "Jupiter", # Sagittarius
        10: "Saturn", # Capricorn
        11: "Saturn", # Aquarius
        12: "Jupiter" # Pisces
    }

    # Debilitation signs
    debilitation = {
        "Moon": 8,   # Scorpio
        "Mars": 4    # Cancer
    }
    
    moon_house = planetData["Moon"]["house"]
    mars_house = planetData["Mars"]["house"]
    moon_sign = planetData["Moon"]["sign"]
    mars_sign = planetData["Mars"]["sign"]

    results = []

    # Step 1: Skip if debilitated
    if moon_sign == debilitation["Moon"] or mars_sign == debilitation["Mars"]:
        return results  

    # Step 2: Detect Chandra–Mangala Yoga
    yoga_detected = False
    if moon_house == mars_house:
        results.append("Chandra–Mangala Yoga (Conjunction)")
        yoga_detected = True
    if (moon_house - mars_house) % 12 == 6:
        results.append("Chandra–Mangala Yoga (Mutual Aspect)")
        yoga_detected = True

    # Step 3: If yoga found, check wealth house rulership
    if yoga_detected:
        wealth_houses = {2, 5, 9, 11}

        # Get ascendant sign from house 1 planetData? (We assume house numbers correspond to chart from Lagna)
        # Find lords of wealth houses
        wealth_house_lords = set()
        for house_num in wealth_houses:
            house_sign = (lagnaSignIndex + house_num) % 12
            if house_sign == 0: 
                house_sign = 12
            wealth_house_lords.add(sign_lords[house_sign])

        if "Moon" in wealth_house_lords or "Mars" in wealth_house_lords:
            results.append("💰 Dhana-oriented Chandra–Mangala Yoga")

    return results

