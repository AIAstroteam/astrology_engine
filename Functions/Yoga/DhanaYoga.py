def findDhanaYogas(planetData: dict, signLords: dict) -> list:
    """
    Detects Dhana Yogas (wealth combinations) in the chart.

    Args:
        planetData (dict): Planet name → {'house': int, 'degree': float, 'sign': int}
        signLords (dict): Sign number (1–12) → lord planet name

    Returns:
        list of Dhana Yogas found.
    """

    # Key houses and groups
    dhanBhava = 2
    labhaBhava = 11
    trikonaHouses = {1, 5, 9}
    kendraHouses = {1, 4, 7, 10}
    benefics = {"Jupiter", "Venus", "Mercury", "Moon"}

    # Mappings
    planetToHouse = {planet: info['house'] for planet, info in planetData.items()}
    planetToSign = {planet: info['sign'] for planet, info in planetData.items()}
    houseToPlanets = {}
    for planet, info in planetData.items():
        house = info['house']
        houseToPlanets.setdefault(house, []).append(planet)

    # House Lords
    houseLords = {}
    for house in range(1, 13):
        occupyingPlanet = next(
            (planet for planet, info in planetData.items() if info['house'] == house),
            None
        )
        sign = planetData[occupyingPlanet]['sign'] if occupyingPlanet else None
        if sign:
            houseLords[house] = signLords.get(sign)

    # Get lords
    lord2 = houseLords.get(2)
    lord11 = houseLords.get(11)
    lord5 = houseLords.get(5)
    lord9 = houseLords.get(9)

    detectedYogas = []

    def isConjunct(p1, p2):
        return p1 in planetToHouse and p2 in planetToHouse and planetToHouse[p1] == planetToHouse[p2]

    def isMutualAspect(p1, p2):
        h1 = planetToHouse.get(p1)
        h2 = planetToHouse.get(p2)
        return h1 and h2 and abs(h1 - h2) == 6

    def isSignExchange(p1, p2):
        return planetToSign.get(p1) == signLords.get(planetToSign.get(p2)) and \
               planetToSign.get(p2) == signLords.get(planetToSign.get(p1))

    # 1. Association of 2nd and 11th lords
    if lord2 and lord11 and lord2 != lord11:
        if isConjunct(lord2, lord11) or isMutualAspect(lord2, lord11) or isSignExchange(lord2, lord11):
            detectedYogas.append("Dhana Yoga: 2nd and 11th lords associated")

    # 2. 2nd lord with 5th or 9th lord
    for dharmaLord in (lord5, lord9):
        if lord2 and dharmaLord and lord2 != dharmaLord:
            if isConjunct(lord2, dharmaLord) or isMutualAspect(lord2, dharmaLord) or isSignExchange(lord2, dharmaLord):
                detectedYogas.append("Dhana Yoga: 2nd lord with 5th or 9th lord")

    # 3. 11th lord with 5th or 9th lord
    for dharmaLord in (lord5, lord9):
        if lord11 and dharmaLord and lord11 != dharmaLord:
            if isConjunct(lord11, dharmaLord) or isMutualAspect(lord11, dharmaLord) or isSignExchange(lord11, dharmaLord):
                detectedYogas.append("Dhana Yoga: 11th lord with 5th or 9th lord")

    # 4. Benefics in 2nd house
    if dhanBhava in houseToPlanets:
        for planet in houseToPlanets[dhanBhava]:
            if planet in benefics:
                detectedYogas.append(f"Dhana Yoga: {planet} (benefic) in 2nd house")

    # 5. 2nd lord in Kendra or Trikona
    if lord2 and planetToHouse.get(lord2) in (kendraHouses | trikonaHouses):
        detectedYogas.append("Dhana Yoga: 2nd lord in Kendra or Trikona")

    # 6. Multiple Dhana Yogas
    if len(detectedYogas) > 1:
        detectedYogas.append("Multiple Dhana Yogas Detected")

    return list(set(detectedYogas))
