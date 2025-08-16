# Define sign lords for classical planets
signLords = {
    1: 'Mars',      # Aries
    2: 'Venus',     # Taurus
    3: 'Mercury',   # Gemini
    4: 'Moon',      # Cancer
    5: 'Sun',       # Leo
    6: 'Mercury',   # Virgo
    7: 'Venus',     # Libra
    8: 'Mars',      # Scorpio
    9: 'Jupiter',   # Sagittarius
    10: 'Saturn',   # Capricorn
    11: 'Saturn',   # Aquarius
    12: 'Jupiter'   # Pisces
}

# Exaltation signs for each planet
exaltationSigns = {
    'Sun': 1,       # Aries
    'Moon': 2,      # Taurus
    'Mars': 10,     # Capricorn
    'Mercury': 6,   # Virgo
    'Jupiter': 4,   # Cancer
    'Venus': 12,    # Pisces
    'Saturn': 7     # Libra
}

# Debilitation signs for each planet
debilitationSigns = {
    'Sun': 7,       # Libra
    'Moon': 8,      # Scorpio
    'Mars': 4,      # Cancer
    'Mercury': 12,  # Pisces
    'Jupiter': 10,  # Capricorn
    'Venus': 6,     # Virgo
    'Saturn': 1     # Aries
}

# Natural malefics
malefics = ['Saturn', 'Mars', 'Rahu', 'Ketu', 'Sun']

def isStrong(planet, pdata):
    """Check if planet is strong: own sign, exalted, kendra/trikona, not debilitated or afflicted."""
    house = pdata[planet]['house']
    sign = pdata[planet]['sign']

    ownSign = (signLords[sign] == planet)
    exalted = (exaltationSigns.get(planet) == sign)
    debilitated = (debilitationSigns.get(planet) == sign)

    # Kendra/trikona positions
    inGoodHouse = house in [1, 4, 7, 10, 5, 9]

    # Affliction check: any malefic in same house
    afflicted = any(
        p != planet and pdata[p]['house'] == house and p in malefics
        for p in pdata
    )

    return (ownSign or exalted) and inGoodHouse and not debilitated and not afflicted

def goodRelationship(planet1, planet2, pdata):
    """Check if planets are conjunct, mutual aspect, or in trine/kendra relationship."""
    h1, h2 = pdata[planet1]['house'], pdata[planet2]['house']
    sameHouse = (h1 == h2)
    kendraRelation = abs(h1 - h2) % 12 in [4, 8]  # 4th or 7th from each other
    trikonaRelation = abs(h1 - h2) % 12 in [5, 9] # 5th or 9th from each other
    return sameHouse or kendraRelation or trikonaRelation

def findLakshmiYoga(pdata, ascSign):
    lagnaLord = signLords[ascSign]
    ninthSign = (ascSign + 8 - 1) % 12 + 1
    ninthLord = signLords[ninthSign]

    lagnaStrong = isStrong(lagnaLord, pdata)
    ninthStrong = isStrong(ninthLord, pdata)
    relationGood = goodRelationship(lagnaLord, ninthLord, pdata)

    return {
        'yoga': lagnaStrong and ninthStrong and relationGood,
        'lagnaLord': lagnaLord,
        'ninthLord': ninthLord,
        'lagnaStrong': lagnaStrong,
        'ninthStrong': ninthStrong,
        'relationGood': relationGood
    }

