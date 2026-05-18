# Oxygen Monitoring System

import random

oxygen_level = random.randint(80, 100)

print("🫁 Oxygen Level:", oxygen_level, "%")

if oxygen_level < 90:
    print("⚠️ Low Oxygen Alert")
else:
    print("✅ Oxygen Level Stable")
