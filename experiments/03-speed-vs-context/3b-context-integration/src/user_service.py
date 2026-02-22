"""User service - intentionally violates several architecture decisions."""

# Violates ADR-003: bare dict instead of TypedDict/dataclass
users_db = {}


# Violates ADR-002: inconsistent naming (camelCase)
def createUser(name, email):  # Violates ADR-003: no type hints
    """Create a new user."""  # Violates ADR-004: missing Args/Returns/Raises
    id = len(users_db) + 1
    users_db[id] = {"name": name, "email": email}
    return users_db[id]


# Violates ADR-001: returns None silently instead of raising ValueError
def get_user(user_id):
    return users_db.get(user_id)


# Violates ADR-001: silently does nothing on invalid input
def delete_user(user_id):
    if user_id in users_db:
        del users_db[user_id]
        return True
    return None  # Violates style guide: inconsistent return type (True/None)


DEFAULT_ROLE = "viewer"


# Violates ADR-002: private function without underscore
def validate_email(email):
    return "@" in email  # Violates ADR-004: no docstring


def update_user(user_id, **kwargs):
    """Update user fields."""
    user = users_db.get(user_id)
    if user:  # Violates style guide: nested if instead of guard clause
        for key, value in kwargs.items():
            user[key] = value
        return user
    # Violates ADR-001: returns None silently
