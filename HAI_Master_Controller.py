"""
Repository: harigovind91/HAI-Hari-AI-
Module: HAI Global Pay / Full System Integration
File: HAI_Master_Controller.py
"""

from 272_Anti_Gravity_Security_Layer import AntiGravityLock
from 273_HAI_Global_Backup_System import HAIBackupSystem
import time

class HAIMasterController:
    def __init__(self):
        self.security = AntiGravityLock()
        self.backup = HAIBackupSystem()
        self.__master_key = "HAI-Admin@786#X" #
        self.system_status = "OFFLINE"

    def boot_system(self, admin_key):
        print("\n--- HAI Millennium Sovereign OS: Booting ---")
        if admin_key != self.__master_key:
            print("🚨 CRITICAL: Unauthorized Access! System Lockdown.")
            return False
        
        self.system_status = "ONLINE"
        print("✅ System Status: ONLINE (Firewall Level-10-Alpha)")
        return True

    def run_daily_maintenance(self, admin_key):
        if self.system_status == "ONLINE":
            print("\n[MAINTENANCE] Running Security Audit and Backup...")
            # सुरक्षा और बैकअप मॉड्यूल को कॉल करना
            self.security.secure_vault("DAILY_LEDGER", admin_key)
            self.backup.create_secure_backup(admin_key)
            print("✅ Maintenance Complete.")
        else:
            print("❌ Error: System must be ONLINE for maintenance.")

# --- सिस्टम ऑपरेशन ---
if __name__ == "__main__":
    hai_os = HAIMasterController()
    
    # 1. सिस्टम को अनलॉक करना
    access_key = input("कृपया मास्टर की (Master Key) दर्ज करें: ")
    
    if hai_os.boot_system(access_key):
        # 2. सभी सुरक्षा और बैकअप फीचर्स को एक साथ चलाना
        hai_os.run_daily_maintenance(access_key)
        
        print("\n[INFO] HAI Global Pay अब पूरी तरह सक्रिय है।")
        print("--- 'Sovereign Control' मोड चालू है ---")
