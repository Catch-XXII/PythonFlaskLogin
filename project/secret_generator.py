import string
import secrets

alphabet = string.ascii_letters + string.digits

def skg() -> str:
    password = "".join(secrets.choice(alphabet) for _ in range(16))
    if (any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(c.isdigit() for c in password) >= 3):
        return password
