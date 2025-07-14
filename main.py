from converter import convert, detect_category, get_target_units, list_all_units
import json
import os
from datetime import datetime

CONFIG_FILE = "config.json"
HISTORY_FILE = "conversion_history.txt"

def load_last_units():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_last_units(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)

def log_history(entry):
    with open(HISTORY_FILE, "a") as f:
        f.write(entry + "\n")

def show_available_units():
    print("\n📚 Valid Input Units by Category:")
    all_units = list_all_units()
    for category, units in all_units.items():
        print(f"  • {category.title()}: {', '.join(units)}")

def start_converter():
    print("=" * 35)
    print("     ADVANCED UNIT CONVERTER v2.0")
    print("=" * 35)

    show_available_units()
    print("\n💡 Enter like: `5 kg`, `12 m`, `100 c`")

    last_used = load_last_units()

    while True:
        user_input = input("\nEnter value with unit (e.g., 5 kg), or 'exit': ").strip().lower()

        if user_input == "exit":
            print("👋 Goodbye!")
            break

        try:
            parts = user_input.split()
            if len(parts) != 2:
                print("⚠️  Please enter in format: <value> <unit> (e.g., 10 m)")
                continue

            value = float(parts[0])
            from_unit = parts[1]

            category = detect_category(from_unit)
            if not category:
                print(f"⚠️  Unit '{from_unit}' not recognized.")
                continue

            targets = get_target_units(from_unit)
            if not targets:
                print(f"⚠️  No available conversions for '{from_unit}'")
                continue

            print(f"\nAvailable conversions for '{from_unit}': {', '.join(targets)}")
            to_unit = input("Convert to: ").strip().lower()

            if to_unit not in targets:
                print("⚠️  Invalid target unit.")
                continue

            result, formula = convert(value, from_unit, to_unit)
            if result is not None:
                print(f"\n✅ {value} {from_unit} = {round(result, 4)} {to_unit}")
                print(f"🔍 Formula used: {formula.replace('x', str(value))}")
                log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {value} {from_unit} -> {result:.4f} {to_unit} | Formula: {formula}"
                log_history(log_entry)

                save_last_units({"last_unit": from_unit})
            else:
                print("⚠️  Conversion not possible.")

        except ValueError:
            print("⚠️  Invalid number format.")

        again = input("\n🔁 Convert another? (y/n): ").strip().lower()
        if again != "y":
            break
        else:
            show_available_units()
            print("\n💡 Enter like: `5 kg`, `12 m`, `100 c`")

if __name__ == "__main__":
    start_converter()
