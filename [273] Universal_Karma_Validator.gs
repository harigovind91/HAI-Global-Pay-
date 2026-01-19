"""
Repository: harigovind91/HAI-Hari-AI-
Module: HAI Global Pay / Advanced Security
File: 273_HAI_Global_Backup_System.py
"""

import shutil
import os
import datetime
import time

class HAIBackupSystem:
    def __init__(self):
        self.source_dir = "./secure_data"     # जहाँ आपका असली डेटा है
        self.backup_dir = "./HAI_Vault_Backup" # जहाँ बैकअप जाएगा
        self.__master_key = "HAI-Admin@786#X"
        
        # बैकअप फोल्डर बनाना अगर नहीं है
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def create_secure_backup(self, admin_key):
        if admin_key != self.__master_key:
            print("🚨 बैकअप विफल: अनधिकृत मास्टर की (Master Key)!")
            return False

        # समय के साथ बैकअप फाइल का नाम (जैसे: HAI_Backup_2026-01-20.zip)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        backup_name = f"HAI_Backup_{timestamp}"
        full_path = os.path.join(self.backup_dir, backup_name)

        try:
            # डेटा को ज़िप (Zip) करके बैकअप लेना
            shutil.make_archive(full_path, 'zip', self.source_dir)
            print(f"✅ बैकअप सफल: {backup_name}.zip सुरक्षित रूप से सेव किया गया।")
            return True
        except Exception as e:
            print(f"❌ एरर: {str(e)}")
            return False

# बैकअप को ऑटो मोड पर चलाना
if __name__ == "__main__":
    backup_tool = HAIBackupSystem()
    print("--- HAI Global Pay: Auto-Backup System Active ---")
    
    # यह उदाहरण के लिए हर 5 सेकंड में चेक करेगा (इसे आप 86400 सेकंड यानी 24 घंटे पर सेट कर सकते हैं)
    while True:
        # यहाँ आप असली की (Key) डालकर इसे ऑटोमेट कर सकते हैं
        backup_tool.create_secure_backup("HAI-Admin@786#X")
        print("⏰ अगला बैकअप 24 घंटे बाद निर्धारित है...")
        time.sleep(86400) 
