import sys
import os

TRIGGER_FILE = "/tmp/virtual_button_trigger"

# Default press type = 0 (Single Press)
press_type = 0

if len(sys.argv) > 1:
    try:
        press_type = int(sys.argv[1])
        if press_type not in [0, 1, 2]:
            raise ValueError("Invalid press type. Use 0 (Single), 1 (Double), 2 (Long).")
    except ValueError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

# Write the press type to the trigger file
with open(TRIGGER_FILE, "w") as f:
    f.write(str(press_type))

print(f"✅ Triggered Virtual Button with press type {press_type}")
