def findViparitaRajaYogas(planetData: dict, signLords: dict) -> list:
    """
    Detects Viparita Raja Yogas from the chart.
    
    Args:
        planetData (dict): Planet → {'house': int, 'degree': float, 'sign': int}
        signLords (dict): Sign → Planet name

    Returns:
        list of detected Viparita Raja Yogas
    """

    # Dusthana houses
    dusthanaHouses = {6, 8, 12}

    # Map planets to their house and sign
    planetToHouse = {planet: data['house'] for planet, data in planetData.items()}
    planetToSign = {planet: data['sign'] for planet, data in planetData.items()}
    houseToPlanets = {}
    for planet, info in planetData.items():
        houseToPlanets.setdefault(info['house'], []).append(planet)

    # Determine lord of each house (via sign)
    houseLords = {}
    for house in range(1, 13):
        # Try to find a planet in the house to get its sign
        planetInHouse = next((p for p in planetData if planetData[p]['house'] == house), None)
        if planetInHouse:
            sign = planetData[planetInHouse]['sign']
            houseLords[house] = signLords.get(sign)

    # Get Dusthana lords
    lord6 = houseLords.get(6)
    lord8 = houseLords.get(8)
    lord12 = houseLords.get(12)
    dusthanaLords = {lord6, lord8, lord12} - {None}

    detectedYogas = []

    # 1. Harsha Yoga: 6th lord in Dusthana
    if lord6 and planetToHouse.get(lord6) in dusthanaHouses:
        detectedYogas.append("Harsha Yoga (6th lord in Dusthana)")

    # 2. Sarala Yoga: 8th lord in Dusthana
    if lord8 and planetToHouse.get(lord8) in dusthanaHouses:
        detectedYogas.append("Sarala Yoga (8th lord in Dusthana)")

    # 3. Vimala Yoga: 12th lord in Dusthana
    if lord12 and planetToHouse.get(lord12) in dusthanaHouses:
        detectedYogas.append("Vimala Yoga (12th lord in Dusthana)")

    # 4. Mutual exchange between two Dusthana lords
    checkedPairs = set()
    for p1 in dusthanaLords:
        for p2 in dusthanaLords:
            if p1 != p2 and (p2, p1) not in checkedPairs:
                if planetToSign.get(p1) == signLords.get(planetToSign.get(p2)) and \
                   planetToSign.get(p2) == signLords.get(planetToSign.get(p1)):
                    detectedYogas.append("Viparita Raja Yoga: Mutual exchange between Dusthana lords")
                checkedPairs.add((p1, p2))

    # 5. Two Dusthana lords conjunct in a Dusthana
    for house, planets in houseToPlanets.items():
        if house in dusthanaHouses:
            found = [p for p in planets if p in dusthanaLords]
            if len(found) >= 2:
                detectedYogas.append("Viparita Raja Yoga: Two Dusthana lords conjunct in Dusthana")

    # 6. Any Dusthana lord in another Dusthana lord’s house
    for p in dusthanaLords:
        house = planetToHouse.get(p)
        if house in dusthanaHouses:
            # Who is the lord of that house?
            houseSign = planetToSign.get(p)
            houseLord = signLords.get(houseSign)
            if houseLord in dusthanaLords and houseLord != p:
                detectedYogas.append("Viparita Raja Yoga: Dusthana lord in another Dusthana lord's house")

    # Remove duplicates and return
    return list(set(detectedYogas))
