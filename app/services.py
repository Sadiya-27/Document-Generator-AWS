"""
Service module.
"""

class UserService:
    """
    Handles user operations.
    """

    def get_user(self, user_id):
        """
        Retrieves user details.

        Args:
            user_id (int): User ID

        Returns:
            dict: User information
        """
        return {
            "id": user_id,
            "name": "Sadiya"
        }