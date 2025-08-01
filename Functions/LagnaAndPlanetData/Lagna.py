import swisseph as swe
from utils import constants as const

def getLagnaSignIndex(julianDay, latitude, longitude):
    swe.set_sid_mode(swe.SIDM_LAHIRI)

    _, ascmc = swe.houses_ex(julianDay, latitude, longitude, b'P', swe.FLG_SIDEREAL)
    ascendantDegree = ascmc[0]
    lagnaSignIndex = int(ascendantDegree // 30)
    lagna = const.zodiacSigns[lagnaSignIndex]
    return lagna, lagnaSignIndex