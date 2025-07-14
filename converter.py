unit_categories = {
    "length": {
        "mm": {"cm": (lambda x: x / 10, "x / 10"), "m": (lambda x: x / 1000, "x / 1000"), "in": (lambda x: x / 25.4, "x / 25.4")},
        "cm": {"mm": (lambda x: x * 10, "x * 10"), "m": (lambda x: x / 100, "x / 100"), "in": (lambda x: x / 2.54, "x / 2.54")},
        "m": {"cm": (lambda x: x * 100, "x * 100"), "km": (lambda x: x / 1000, "x / 1000"), "ft": (lambda x: x * 3.28084, "x * 3.28084")},
        "km": {"m": (lambda x: x * 1000, "x * 1000"), "mi": (lambda x: x / 1.609, "x / 1.609")},
        "in": {"cm": (lambda x: x * 2.54, "x * 2.54"), "ft": (lambda x: x / 12, "x / 12")},
        "ft": {"in": (lambda x: x * 12, "x * 12"), "m": (lambda x: x / 3.28084, "x / 3.28084")},
        "mi": {"km": (lambda x: x * 1.609, "x * 1.609")}
    },
    "mass": {
        "mg": {"g": (lambda x: x / 1000, "x / 1000")},
        "g": {"mg": (lambda x: x * 1000, "x * 1000"), "kg": (lambda x: x / 1000, "x / 1000")},
        "kg": {"g": (lambda x: x * 1000, "x * 1000"), "lb": (lambda x: x * 2.20462, "x * 2.20462")},
        "lb": {"kg": (lambda x: x / 2.20462, "x / 2.20462"), "oz": (lambda x: x * 16, "x * 16")},
        "oz": {"lb": (lambda x: x / 16, "x / 16")}
    },
    "temperature": {
        "c": {
            "f": (lambda x: x * 9/5 + 32, "(x * 9/5) + 32"),
            "k": (lambda x: x + 273.15, "x + 273.15")
        },
        "f": {
            "c": (lambda x: (x - 32) * 5/9, "(x - 32) * 5/9")
        },
        "k": {
            "c": (lambda x: x - 273.15, "x - 273.15")
        }
    },
    "force": {
        "n": {"lbf": (lambda x: x * 0.224809, "x * 0.224809")},
        "lbf": {"n": (lambda x: x / 0.224809, "x / 0.224809")}
    },
    "pressure": {
        "pa": {"kpa": (lambda x: x / 1000, "x / 1000"), "psi": (lambda x: x / 6895, "x / 6895")},
        "kpa": {"pa": (lambda x: x * 1000, "x * 1000")},
        "psi": {"pa": (lambda x: x * 6895, "x * 6895")}
    },
    "energy": {
        "j": {"kj": (lambda x: x / 1000, "x / 1000"), "cal": (lambda x: x / 4.184, "x / 4.184")},
        "kj": {"j": (lambda x: x * 1000, "x * 1000")},
        "cal": {"j": (lambda x: x * 4.184, "x * 4.184")}
    },
    "power": {
        "w": {"kw": (lambda x: x / 1000, "x / 1000"), "hp": (lambda x: x / 745.7, "x / 745.7")},
        "kw": {"w": (lambda x: x * 1000, "x * 1000")},
        "hp": {"w": (lambda x: x * 745.7, "x * 745.7")}
    }
}

def detect_category(unit):
    for category, units in unit_categories.items():
        if unit in units:
            return category
    return None

def get_target_units(unit):
    category = detect_category(unit)
    if category and unit in unit_categories[category]:
        return list(unit_categories[category][unit].keys())
    return []

def convert(value, from_unit, to_unit):
    category = detect_category(from_unit)
    if category and from_unit in unit_categories[category]:
        converters = unit_categories[category][from_unit]
        if to_unit in converters:
            func, formula = converters[to_unit]
            return func(value), formula
    return None, None

def list_all_units():
    result = {}
    for category, units in unit_categories.items():
        result[category] = list(units.keys())
    return result
