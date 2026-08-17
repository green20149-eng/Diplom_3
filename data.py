import uuid

class UserData:
    PASSWORD = "TestPassword123"

    @staticmethod
    def generate_user():
        unique_id = uuid.uuid4().hex
        return {
            "email": f"stellar_{unique_id}@example.com",
            "password": UserData.PASSWORD,
            "name": "Test User",
        }
