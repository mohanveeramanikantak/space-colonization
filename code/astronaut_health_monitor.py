# Astronaut Health Monitoring System

import random
import time

print("👨‍🚀 Astronaut Health Monitoring Started")

time.sleep(1)

# Simulated health data
heart_rate = random.randint(55, 120)
oxygen_level = random.randint(85, 100)
body_temperature = round(random.uniform(35.5, 39.0), 1)

# Display health readings
print("❤️ Heart Rate:", heart_rate, "BPM")
print("🫁 Oxygen Level:", oxygen_level, "%")
print("🌡 Body Temperature:", body_temperature, "°C")

time.sleep(1)

# Health analysis
if heart_rate > 100:
    print("⚠️ High Heart Rate Detected")

if oxygen_level < 90:
    print("⚠️ Low Oxygen Warning")

if body_temperature > 37.5:
    print("🔥 High Body Temperature Alert")

# Final status
if heart_rate <= 100 and oxygen_level >= 90 and body_temperature <= 37.5:
    print("✅ Astronaut Health Stable")
else:
    print("🚨 Medical Attention Recommended")
