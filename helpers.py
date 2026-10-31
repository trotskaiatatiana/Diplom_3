
import uuid


class Helpers:
    @staticmethod
    def generate_user_data():
        return {
            "email": f"test_{uuid.uuid4().hex[:10]}@example.com",
            "password": "TestPassword123",
            "name": "Test User"
        }
