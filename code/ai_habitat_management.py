# AI Habitat Management System

import random
import time

print("🏠 AI Habitat Management System Started")

time.sleep(1)

# Simulated habitat data
oxygen_level = random.randint(80, 100)
temperature = random.randint(15, 35)
power_level = random.randint(40, 100)

# Display habitat status
print("🫁 Oxygen Level:", oxygen_level, "%")
print("🌡 Temperature:", temperature, "°C")
print("🔋 Power Level:", power_level, "%")

time.sleep(1)

# AI management decisions
if oxygen_level < 90:
    print("⚠️ Low Oxygen Detected")
    print("✅ Activating Oxygen Support System")

if temperature < 18:
    print("❄️ Temperature Too Low")
    print("🔥 Activating Heating System")

elif temperature > 30:
    print("🔥 Temperature Too High")
    print("❄️ Activating Cooling System")

if power_level < 50:
    print("⚠️ Low Power Warning")
    print("🔋 Switching to Backup Power")

# Final habitat status
if oxygen_level >= 90 and 18 <= temperature <= 30 and power_level >= 50:
    print("✅ Habitat Conditions Stable")

print("🚀 Habitat Monitoring Completed")
