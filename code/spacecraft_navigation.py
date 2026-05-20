# Spacecraft Navigation Simulation

import random
import time

print("🚀 Spacecraft Navigation System Started")

time.sleep(1)

# Possible navigation directions
directions = [
    "Move Forward",
    "Adjust Left",
    "Adjust Right",
    "Increase Altitude",
    "Decrease Altitude"
]

# Random navigation command
command = random.choice(directions)

# Simulated obstacle distance
distance = random.randint(10, 100)

print("Navigation Command:", command)
print("Obstacle Distance:", distance, "km")

time.sleep(1)

# Navigation decision
if distance < 30:
    print("⚠️ Obstacle Nearby")
    print("🔄 Changing Route")

else:
    print("✅ Path Clear")
    print("🛰 Continuing Mission")

print("🚀 Navigation Process Completed")
