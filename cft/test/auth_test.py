import pytest
from sqlalchemy import insert, select
from fastapi import Depends

from conf_test import client, async_session_maker
from main import fastapi_users
from src.auth.database import User


# async def test_add_role():
#     async with async_session_maker() as session:
#         stmt = insert(role).values(id=1, name="admin", permissions=None)
#         await session.execute(stmt)
#         await session.commit()
#
#         query = select(role)
#         result = await session.execute(query)
#         assert result.all() == [(1, 'admin', None)], "Роль не добавилась"


current_user = fastapi_users.current_user()


def test_register():
    response = client.post("/auth/register", json={
        "email": "string",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "last_name": "string",
        "first_name": "string",
        "date_next_promt": '2024-06-12',
        "salary": 12000
    })

    assert response.status_code == 201
