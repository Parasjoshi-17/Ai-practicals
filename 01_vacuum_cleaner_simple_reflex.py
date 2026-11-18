"""Practical 1: Simple reflex agent for the Vacuum Cleaner world."""
rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"

while True:
    print(f"\nLocation: {location} | Current room: {rooms[location]}")
    if rooms[location] == "Dirty":
        action = "SUCK"
        rooms[location] = "Clean"
    elif location == "A":
        action = "RIGHT"
        location = "B"
    else:
        action = "STOP"

    print("Action:", action)
    if action == "STOP":
        break

print("Final room status:", rooms)
