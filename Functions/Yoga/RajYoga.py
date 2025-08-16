def findRajaYogas(planetData: dict, signLords: dict) -> list:
    """
    Detects Raja Yogas from planetary positions.

    Args:
        planetData (dict): Dict mapping planet name to its house, sign, and degree.
        signLords (dict): Dict mapping sign number (1–12) to the lord planet.

    Returns:
        list: List of detected Raja Yogas with descriptions.
    """

    kendraHouses = {1, 4, 7, 10}
    trikonaHouses = {1, 5, 9}
    benefics = {"Jupiter", "Venus", "Mercury", "Moon"}

    # Map house → planets, planet → house, planet → sign
    houseToPlanets = {}
    planetToHouse = {}
    planetToSign = {}

    for planet, details in planetData.items():
        house = details["house"]
        sign = details["sign"]

        houseToPlanets.setdefault(house, []).append(planet)
        planetToHouse[planet] = house
        planetToSign[planet] = sign

    # Map house number → house lord (based on sign and signLords)
    houseLords = {}
    for house in range(1, 13):
        sign = None
        for planet, details in planetData.items():
            if details["house"] == house:
                sign = details["sign"]
                break
        if sign:
            houseLords[house] = signLords[sign]

    detectedYogas = []

    def isConjunct(p1, p2):
        return planetToHouse.get(p1) == planetToHouse.get(p2)

    def isMutualAspect(p1, p2):
        h1 = planetToHouse.get(p1)
        h2 = planetToHouse.get(p2)
        return h1 and h2 and abs(h1 - h2) == 6

    def isSignExchange(p1, p2):
        return planetToSign.get(p1) == signLords.get(planetToSign.get(p2)) and \
               planetToSign.get(p2) == signLords.get(planetToSign.get(p1))

    # 1. Kendra-Trikona Raja Yoga
    for kendra in kendraHouses:
        kendraLord = houseLords.get(kendra)
        if not kendraLord:
            continue
        for trikona in trikonaHouses:
            trikonaLord = houseLords.get(trikona)
            if not trikonaLord or kendraLord == trikonaLord:
                continue
            if isConjunct(kendraLord, trikonaLord):
                detectedYogas.append("Kendra-Trikona Raja Yoga (Conjunction)")
            elif isMutualAspect(kendraLord, trikonaLord):
                detectedYogas.append("Kendra-Trikona Raja Yoga (Mutual Aspect)")
            elif isSignExchange(kendraLord, trikonaLord):
                detectedYogas.append("Parivartana Raja Yoga")

    # 2. Dharma-Karmadhipati Yoga (9th lord and 10th lord association)
    lord9 = houseLords.get(9)
    lord10 = houseLords.get(10)
    if lord9 and lord10 and lord9 != lord10:
        if isConjunct(lord9, lord10) or isMutualAspect(lord9, lord10) or isSignExchange(lord9, lord10):
            detectedYogas.append("Dharma-Karmadhipati Yoga")

    # 3. Rajya Poojit Raja Yoga
    for planet in benefics:
        if planet not in planetToHouse:
            continue
        if planetToHouse[planet] in kendraHouses:
            for trikona in trikonaHouses:
                trikonaLord = houseLords.get(trikona)
                if trikonaLord and trikonaLord != planet:
                    if isConjunct(planet, trikonaLord) or isMutualAspect(planet, trikonaLord):
                        detectedYogas.append("Rajya Poojit Raja Yoga")

    # 4. Multiple Raja Yogas
    if len(detectedYogas) > 1:
        detectedYogas.append("Multiple Raja Yogas Detected")

    return list(set(detectedYogas))
