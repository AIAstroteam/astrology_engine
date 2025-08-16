import swisseph as swe
from utils import constants as const
import Functions.LagnaAndPlanetData.Lagna as lg

def getLagnaAndPlanetHouses(julianDay, latitude, longitude):

    # --- Set Lahiri ayanamsa for Vedic astrology ---
    swe.set_sid_mode(swe.SIDM_LAHIRI)

    planetDegrees = getPlanetDegrees(julianDay)

    # --- Calculate Ascendant ---
    lagna, lagnaSignIndex  = lg.getLagnaSignIndex(julianDay, latitude, longitude)

    # --- Map house numbers to zodiac signs (starting from Lagna) ---
    houseSigns = [const.zodiacSigns[(lagnaSignIndex + i) % 12] for i in range(12)]
    houseSignsIndex = [(lagnaSignIndex + i) % 12 for i in range(12)]

    # --- Assign planets to houses (Whole Sign System) ---
    planetHouses = {}
    for name, degree in planetDegrees.items():
        planetSign = int(degree // 30)
        house = ((planetSign - lagnaSignIndex) % 12) + 1
        sign =  12 if houseSignsIndex[house] == 0 else houseSignsIndex[house]
        planetHouses[name] = {
            "house": house,
            "degree": round(degree, 6),
            "sign": sign
        }

    return lagnaSignIndex, planetHouses


# --- Calculate sidereal degrees of planets ---
def getPlanetDegrees(julianDay):
    swe.set_sid_mode(swe.SIDM_LAHIRI)

    planetDegrees = {}
    for id, name in const.planetIds.items():
        position, _ = swe.calc_ut(julianDay, id, swe.FLG_SIDEREAL)
        planetDegrees[name] = position[0]

    # --- Add Ketu manually (opposite to Rahu) ---
    ketuDegree = (planetDegrees["Rahu"] + 180.0) % 360.0
    planetDegrees["Ketu"] = ketuDegree

    return planetDegrees

