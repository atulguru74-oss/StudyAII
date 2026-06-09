import bcrypt
from database import add_user, get_user


def hash_password(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


def verify_password(password, hashed):
    return bcrypt.checkpw(
        password.encode(),
        hashed.encode()
    )


def register(username, password):

    existing = get_user(username)

    if existing:
        return False, "Username already exists"

    hashed = hash_password(password)

    add_user(username, hashed)

    return True, "Registration Successful"


def login(username, password):

    user = get_user(username)

    if not user:
        return False

    stored_hash = user[2]

    if verify_password(password, stored_hash):
        return True

    return False