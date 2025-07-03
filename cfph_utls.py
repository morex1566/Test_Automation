def parseNumber(text):
    try:
        return int(text.strip().replace(",", ""))
    except ValueError:
        return None
    

    weaponDatasItem = {
    "Category": None,
    "Weapon": None,
    "Price": None,
    "Price Type": None
}
    
    checklistItem = {
    "No": None,
    "Depth 1": None,
    "Depth 2": None,
    "Depth 3": None,
    "Depth 4": None,
    "Checkpoint": None,
    "Result": None
}