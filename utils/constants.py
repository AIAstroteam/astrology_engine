
# Default location settings
DEFAULT_LATITUDE = 28.6139  # Delhi, India
DEFAULT_LONGITUDE = 77.2090
DEFAULT_TIMEZONE = "Asia/Kolkata"

# Swiss Ephemeris settings
SWISSEPH_PATH = None  # Will use default path
EPHEMERIS_FILES = [
    "seas_18.se1",  # Swiss Ephemeris Asteroid File
    "semo_18.se1",  # Swiss Ephemeris Moon File
    "sepl_18.se1",  # Swiss Ephemeris Planet File
]

# Planetary constants
planetIds = {
    0: "Sun",
    1: "Moon",
    2: "Mercury",
    3: "Venus",
    4: "Mars",
    5: "Jupiter",
    6: "Saturn",
    7: "Uranus",
    8: "Neptune",
    9: "Pluto",
    10: "Rahu"
}

# Zodiac signs
zodiacSigns = [
    'Aries', 'Taurus', 'Gemini', 'Cancer', 
    'Leo', 'Virgo', 'Libra', 'Scorpio',
    'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
]

# Nakshatras (Lunar Mansions)
nakshatrasAndRulingPlanets = [
    ("Ashwini", "Ketu"), ("Bharani", "Venus"), ("Krittika", "Sun"), ("Rohini", "Moon"),
    ("Mrigashira", "Mars"), ("Ardra", "Rahu"), ("Punarvasu", "Jupiter"), ("Pushya", "Saturn"),
    ("Ashlesha", "Mercury"), ("Magha", "Ketu"), ("Purva Phalguni", "Venus"), ("Uttara Phalguni", "Sun"),
    ("Hasta", "Moon"), ("Chitra", "Mars"), ("Swati", "Rahu"), ("Vishakha", "Jupiter"),
    ("Anuradha", "Saturn"), ("Jyeshtha", "Mercury"), ("Mula", "Ketu"), ("Purva Ashadha", "Venus"),
    ("Uttara Ashadha", "Sun"), ("Shravana", "Moon"), ("Dhanishta", "Mars"), ("Shatabhisha", "Rahu"),
    ("Purva Bhadrapada", "Jupiter"), ("Uttara Bhadrapada", "Saturn"), ("Revati", "Mercury")
]

signType = {
    "Aries": "Movable", "Cancer": "Movable", "Libra": "Movable", "Capricorn": "Movable",
    "Taurus": "Fixed", "Leo": "Fixed", "Scorpio": "Fixed", "Aquarius": "Fixed",
    "Gemini": "Dual", "Virgo": "Dual", "Sagittarius": "Dual", "Pisces": "Dual"
}

oldSigns = [0, 2, 4, 6, 8, 10]

signLords = {
    1: "Mars", 2: "Venus", 3: "Mercury", 4: "Moon",
    5: "Sun", 6: "Mercury", 7: "Venus", 8: "Mars",
    9: "Jupiter", 10: "Saturn", 11: "Saturn", 12: "Jupiter"
}

# Calculation settings
DEFAULT_SYSTEM = 'Tropical'  # or 'Sidereal'
AYANAMSA = 23.85  # Lahiri Ayanamsa (degrees)

# Output settings
OUTPUT_FORMAT = 'json'  # 'json' or 'dict'
INCLUDE_DETAILS = True
INCLUDE_POSITIONS = True

# Dasha settings
DASHA_SYSTEM = 'Vimshottari'  # or 'Ashtottari', 'Yogini'
MAHADASHA_YEARS = {
    'Sun': 6, 'Moon': 10, 'Mars': 7, 'Rahu': 18,
    'Jupiter': 16, 'Saturn': 19, 'Mercury': 17, 'Ketu': 7, 'Venus': 20
}

# House system
HOUSE_SYSTEM = 'Placidus'  # or 'Koch', 'Equal', 'Whole Sign'

# Divisional charts
DIVISIONAL_CHARTS = {
    'D-1': 1,    # Rashi Chart
    'D-2': 2,    # Hora Chart
    'D-3': 3,    # Drekkana Chart
    'D-4': 4,    # Chaturthamsa Chart
    'D-7': 7,    # Saptamsa Chart
    'D-9': 9,    # Navamsa Chart
    'D-10': 10,  # Dashamsa Chart
    'D-12': 12,  # Dwadashamsa Chart
    'D-16': 16,  # Shodashamsa Chart
    'D-20': 20,  # Vimsamsa Chart
    'D-24': 24,  # Chaturvimsamsa Chart
    'D-27': 27,  # Saptavimsamsa Chart
    'D-30': 30,  # Trimsamsa Chart
    'D-40': 40,  # Khavedamsa Chart
    'D-45': 45,  # Akshavedamsa Chart
    'D-60': 60,  # Shashtiamsa Chart
} 

# Zodiac sign degrees (starting from Aries 0°)
ZODIAC_DEGREES = {
    'Aries': (0, 30),
    'Taurus': (30, 60),
    'Gemini': (60, 90),
    'Cancer': (90, 120),
    'Leo': (120, 150),
    'Virgo': (150, 180),
    'Libra': (180, 210),
    'Scorpio': (210, 240),
    'Sagittarius': (240, 270),
    'Capricorn': (270, 300),
    'Aquarius': (300, 330),
    'Pisces': (330, 360)
}

# Nakshatra degrees (each spans 13°20')
NAKSHATRA_DEGREES = {
    'Ashwini': (0, 13.3333),
    'Bharani': (13.3333, 26.6667),
    'Krittika': (26.6667, 40),
    'Rohini': (40, 53.3333),
    'Mrigashira': (53.3333, 66.6667),
    'Ardra': (66.6667, 80),
    'Punarvasu': (80, 93.3333),
    'Pushya': (93.3333, 106.6667),
    'Ashlesha': (106.6667, 120),
    'Magha': (120, 133.3333),
    'Purva Phalguni': (133.3333, 146.6667),
    'Uttara Phalguni': (146.6667, 160),
    'Hasta': (160, 173.3333),
    'Chitra': (173.3333, 186.6667),
    'Swati': (186.6667, 200),
    'Vishakha': (200, 213.3333),
    'Anuradha': (213.3333, 226.6667),
    'Jyeshtha': (226.6667, 240),
    'Mula': (240, 253.3333),
    'Purva Ashadha': (253.3333, 266.6667),
    'Uttara Ashadha': (266.6667, 280),
    'Shravana': (280, 293.3333),
    'Dhanishta': (293.3333, 306.6667),
    'Shatabhisha': (306.6667, 320),
    'Purva Bhadrapada': (320, 333.3333),
    'Uttara Bhadrapada': (333.3333, 346.6667),
    'Revati': (346.6667, 360)
}

# Planetary rulerships
PLANETARY_RULERSHIPS = {
    'Sun': 'Leo',
    'Moon': 'Cancer',
    'Mercury': ['Gemini', 'Virgo'],
    'Venus': ['Taurus', 'Libra'],
    'Mars': ['Aries', 'Scorpio'],
    'Jupiter': ['Sagittarius', 'Pisces'],
    'Saturn': ['Capricorn', 'Aquarius']
}

# Element associations
ELEMENTS = {
    'Fire': ['Aries', 'Leo', 'Sagittarius'],
    'Earth': ['Taurus', 'Virgo', 'Capricorn'],
    'Air': ['Gemini', 'Libra', 'Aquarius'],
    'Water': ['Cancer', 'Scorpio', 'Pisces']
}

# Quality associations
QUALITIES = {
    'Cardinal': ['Aries', 'Cancer', 'Libra', 'Capricorn'],
    'Fixed': ['Taurus', 'Leo', 'Scorpio', 'Aquarius'],
    'Mutable': ['Gemini', 'Virgo', 'Sagittarius', 'Pisces']
}

# House meanings
HOUSE_MEANINGS = {
    1: 'Self, personality, appearance',
    2: 'Wealth, family, speech',
    3: 'Siblings, courage, short journeys',
    4: 'Mother, home, property',
    5: 'Children, intelligence, romance',
    6: 'Health, enemies, service',
    7: 'Marriage, partnerships, open enemies',
    8: 'Longevity, obstacles, occult',
    9: 'Religion, guru, higher learning',
    10: 'Career, father, authority',
    11: 'Income, gains, elder siblings',
    12: 'Expenses, losses, foreign travel'
}

# Aspect orbs (degrees)
ASPECT_ORBS = {
    'Conjunction': 10,
    'Opposition': 8,
    'Trine': 8,
    'Square': 8,
    'Sextile': 6
}

# Retrograde planets (Swiss Ephemeris flags)
RETROGRADE_FLAG = 0x8000

# Calculation precision
DEGREE_PRECISION = 4
POSITION_PRECISION = 2 