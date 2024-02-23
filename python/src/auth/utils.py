import jwt
import datetime


def create_token(username, secret_key, admin):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": admin,
        },
        secret_key,
        algorithm="HS256",  # HMAC-SHA256 is default algorithm
    )
