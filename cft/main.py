import uvicorn
from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from src.auth.auth import auth_backend
from src.auth.database import User
from src.auth.manager import get_user_manager
from src.auth.shemas import UserRead, UserCreate

app = FastAPI(
    title='ШИФТ ЦФТ',
    version='0.3'
)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


current_user = fastapi_users.current_user()


@app.get("/protected-route-get-data")
def protected_route(user: User = Depends(current_user)):
    return {
        "date of the next promotion": user.date_next_promt
    }


@app.get("/protected-route-get-salary")
def protected_route(user: User = Depends(current_user)):
    return {
        "curent salary": user.salary
    }


if __name__ == '__main__':
    uvicorn.run(app=app, reload_includes="True")
