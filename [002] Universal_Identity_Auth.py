import hashlib

class UserIdentity:
    def __init__(self, citizen_id, biometric_hash):
        self.citizen_id = citizen_id
        self.auth_token = self.generate_token(biometric_hash)

    def generate_token(self, bio):
        return hashlib.sha256(f"{self.citizen_id}{bio}".encode()).hexdigest()

    def verify_access(self, input_token):
        return self.auth_token == input_token
      
