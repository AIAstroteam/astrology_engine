def findGajaKesariYoga(planetData):
    """
    Detects Gaja Kesari Yoga:
    Jupiter in Kendra (1, 4, 7, 10) from Moon and not debilitated.
    """
    yogas = []
    
    # Debilitation sign for Jupiter = Capricorn (10)
    debilitatedSignForJupiter = 10

    # Get Moon and Jupiter positions
    if "Moon" not in planetData or "Jupiter" not in planetData:
        return yogas  # Can't check without both planets
    
    moonHouse = planetData["Moon"]["house"]
    jupiterHouse = planetData["Jupiter"]["house"]
    jupiterSign = planetData["Jupiter"]["sign"]
    
    # Calculate house distance from Moon to Jupiter (1-12 range)
    distance = ((jupiterHouse - moonHouse) % 12) + 1
    
    # Kendra positions from Moon: 1, 4, 7, 10
    if distance in [1, 4, 7, 10]:
        if jupiterSign != debilitatedSignForJupiter:
            yogas.append("Gaja Kesari Yoga")
    
    return yogas
