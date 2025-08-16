from typing import Dict, List

# Define constants
signs = {
    1: "Aries", 2: "Taurus", 3: "Gemini", 4: "Cancer",
    5: "Leo", 6: "Virgo", 7: "Libra", 8: "Scorpio",
    9: "Sagittarius", 10: "Capricorn", 11: "Aquarius", 12: "Pisces"
}

kendraHouses = [1, 4, 7, 10]

# Planet's own and exalted signs
mahaPurushaConditions = {
    "Mars": {
        "ownSigns": [1, 8],       # Aries, Scorpio
        "exaltedSign": 10,        # Capricorn
        "yoga": "Ruchaka Yoga"
    },
    "Mercury": {
        "ownSigns": [3, 6],       # Gemini, Virgo
        "exaltedSign": 6,         # Virgo
        "yoga": "Bhadra Yoga"
    },
    "Jupiter": {
        "ownSigns": [9, 12],      # Sagittarius, Pisces
        "exaltedSign": 4,         # Cancer
        "yoga": "Hamsa Yoga"
    },
    "Venus": {
        "ownSigns": [2, 7],       # Taurus, Libra
        "exaltedSign": 12,        # Pisces
        "yoga": "Malavya Yoga"
    },
    "Saturn": {
        "ownSigns": [10, 11],     # Capricorn, Aquarius
        "exaltedSign": 7,         # Libra
        "yoga": "Shasha Yoga"
    }
}

def detectMahaPurushaYogas(lagnaChart):
    """Detects Maha Purusha Yogas in the provided Lagna chart."""
    detectedYogas = []

    for planet, data in lagnaChart.items():
        if planet not in mahaPurushaConditions:
            continue

        sign = data.get("sign")
        house = data.get("house")

        if sign is None or house is None:
            continue  # Incomplete data, skip

        yogaInfo = mahaPurushaConditions[planet]

        if house in kendraHouses and (sign in yogaInfo["ownSigns"] or sign == yogaInfo["exaltedSign"]):
            detectedYogas.append({
                "yoga": yogaInfo["yoga"],
                "planet": planet,
                "sign": signs[sign],
                "house": house
            })

    return detectedYogas