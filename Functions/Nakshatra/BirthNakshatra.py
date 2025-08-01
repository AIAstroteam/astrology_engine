from utils import constants as const

def getBirthNakshatra(moon_deg):
    nakshatraLength = 13.3333
    padaLength = 3.3333

    idx = int(moon_deg / nakshatraLength)
    pada = int((moon_deg % nakshatraLength) / padaLength) + 1

    nakshartaName, rulingPlanet = const.nakshatrasAndRulingPlanets[idx]
    return {
        "nakshatra": nakshartaName,
        "pada": pada,
        "rulingPlanet": rulingPlanet
    }