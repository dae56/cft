from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

from settings.config import SECRET_1


cookie_transport = CookieTransport(cookie_name='shft', cookie_max_age=40)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_1, lifetime_seconds=800)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
