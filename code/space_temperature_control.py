# Space Habitat Temperature Control

import random

temperature = random.randint(-20, 40)

print("🌡 Habitat Temperature:", temperature, "°C")

if temperature < 0:
    print("❄️ Activating Heating System")

elif temperature > 30:
    print("🔥 Activating Cooling System")

else:
    print("✅ Temperature Stable")
