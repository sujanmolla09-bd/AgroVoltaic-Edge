import os
import time
import csv
import random
from datetime import datetime

# CSV ফাইলের নাম ও ডিরেক্টরি সেটআপ
LOG_FILE = "agrovoltaic_telemetry.csv"

def init_csv():
    """CSV ফাইল না থাকলে ফাইল এবং হেডার রো তৈরি করবে"""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Soil_Moisture_%", "Ambient_Temp_C", "Sunlight_%", "Irrigation_Status", "Solar_Action", "Alert_Status"])

def read_sensor_data():
    """এগ্রি-ভোল্টাইক ফিল্ডের সেন্সর থেকে সিমুলেটেড ডেটা গ্রহণ"""
    return {
        "soil_moisture": round(random.uniform(15.0, 45.0), 1),
        "ambient_temp": round(random.uniform(28.0, 42.0), 1),
        "sunlight_intensity": round(random.uniform(60.0, 98.0), 1)
    }

def process_ai_logic(data):
    """সেন্সর ডেটার ভিত্তিতে অটোমেটিক সিদ্ধান্ত গ্রহণ ও অ্যালার্ট চেক"""
    actions = []
    irrigation_status = ""
    solar_action = ""
    alert_status = "NORMAL"
    
    # ১. সেচ ব্যবস্থার লজিক
    if data["soil_moisture"] < 30.0 and data["ambient_temp"] > 30.0:
        irrigation_status = "PUMP_ON"
        actions.append("ACTION: Turn ON Smart Irrigation (Water Pump Activated)")
    else:
        irrigation_status = "PUMP_OFF"
        actions.append("STATUS: Soil Moisture Optimal (Irrigation OFF)")

    # ২. সোলার ট্র্যাকিং লজিক
    if data["sunlight_intensity"] > 75.0:
        solar_action = "ANGLE_45_DEG"
        actions.append("ACTION: Adjust Panel Angle to 45° for Maximum Power")
    else:
        solar_action = "FLAT_FOR_CROPS"
        actions.append("ACTION: Flatten Panels to Allow Crop Sunlight Pass-through")

    # ৩. জরুরি অ্যালার্ট সিস্টেম (High Threshold Detection)
    if data["ambient_temp"] > 38.0:
        alert_status = "CRITICAL_HEAT_WAVE"
        actions.append("⚠️ ALERT: Extreme Temperature Detected! Activating Crop Cooling Misters.")
    elif data["soil_moisture"] < 20.0:
        alert_status = "CRITICAL_DROUGHT_RISK"
        actions.append("⚠️ ALERT: Severe Drought Risk Detected! Escalating Irrigation Flow.")

    return actions, irrigation_status, solar_action, alert_status

def log_data_to_csv(timestamp, data, irrigation_status, solar_action, alert_status):
    """লগ ডেটা CSV ফাইলে সেভ করার ফাংশন"""
    with open(LOG_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            timestamp,
            data["soil_moisture"],
            data["ambient_temp"],
            data["sunlight_intensity"],
            irrigation_status,
            solar_action,
            alert_status
        ])

def run_agent():
    print("=== AgroVoltaic-Edge Autonomous AI Agent Active ===")
    print(f"Logging data continuously to: {LOG_FILE}\n")
    
    init_csv()
    
    try:
        while True:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sensor_data = read_sensor_data()
            decisions, irr_stat, solar_act, alert_stat = process_ai_logic(sensor_data)
            
            # CSV ফাইলে ডাটা রাইট করা
            log_data_to_csv(current_time, sensor_data, irr_stat, solar_act, alert_stat)
            
            print(f"[{current_time}] Sensor Telemetry: {sensor_data}")
            for decision in decisions:
                print(f"  └─ {decision}")
            print(f"  └─ 💾 [Logged to {LOG_FILE}]")
            print("-" * 60)
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nAgent monitoring and data logging stopped safely.")

if __name__ == "__main__":
    run_agent()