import hashlib
import os

class UserIdentity:
    def __init__(self, citizen_id, biometric_data):
        self.citizen_id = citizen_id
        # आपकी मास्टर की को 'Salt' की तरह उपयोग करना सुरक्षा को 10x बढ़ा देता है
        self.__secret_salt = "HAI-Admin@786#X" 
        self.auth_token = self.generate_token(biometric_data)

    def generate_token(self, bio):
        # Biometric + ID + MasterKey को मिलाकर एक अद्वितीय (Unique) टोकन बनाना
        raw_data = f"{self.citizen_id}{bio}{self.__secret_salt}"
        return hashlib.sha256(raw_data.encode()).hexdigest()

    def verify_access(self, input_bio):
        # इनपुट किए गए बायोमेट्रिक से नया टोकन बनाकर मैच करना (ज्यादा सुरक्षित तरीका)
        check_token = self.generate_token(input_bio)
        return self.auth_token == check_token

# इस्तेमाल करने का तरीका
user = UserIdentity("HARI_CEO_01", "FINGERPRINT_DATA_99")
print(f"Generated HAI-Token: {user.auth_token}")

# एक्सेस की जांच
if user.verify_access("FINGERPRINT_DATA_99"):
    print("✅ Identity Verified: Sovereign Access Granted.")
else:
    print("❌ Identity Mismatch: Alerting Security.")
        
