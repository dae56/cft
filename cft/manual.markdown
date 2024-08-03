# Файл с тестовым заданием
Файл с тестовым заданием находится по ссылке: `https://drive.google.com/file/d/1aNctqjsy0IuyqA-d7rsTz4-zwvLhebSD/view`
# Подготовка и запуск проекта:
Первым делом необходимо скачать проект из репозитория и установить все зависимости через poetry. Список зависимостей есть в файле pyproject.toml и requirments.txt
Так же предоставляю дерево зависимостей:
``````
alembic 1.13.1 A database migration tool for SQLAlchemy.
├── mako *
│   └── markupsafe >=0.9.2
├── sqlalchemy >=1.3.0
│   ├── greenlet !=0.4.17
│   └── typing-extensions >=4.6.0
└── typing-extensions >=4
asyncpg 0.29.0 An asyncio PostgreSQL driver
└── async-timeout >=4.0.3
fastapi 0.111.0 FastAPI framework, high performance, easy to learn, fast to code, ready for production
├── email-validator >=2.0.0
│   ├── dnspython >=2.0.0
│   └── idna >=2.0.0
├── fastapi-cli >=0.0.2
│   ├── fastapi * (circular dependency aborted here)
│   ├── typer >=0.12.3
│   │   ├── click >=8.0.0
│   │   │   └── colorama *
│   │   ├── rich >=10.11.0
│   │   │   ├── markdown-it-py >=2.2.0
│   │   │   │   └── mdurl >=0.1,<1.0
│   │   │   └── pygments >=2.13.0,<3.0.0
│   │   ├── shellingham >=1.3.0
│   │   └── typing-extensions >=3.7.4.3
│   └── uvicorn >=0.15.0
│       ├── click >=7.0 (circular dependency aborted here)
│       ├── colorama >=0.4 (circular dependency aborted here)
│       ├── h11 >=0.8
│       ├── httptools >=0.5.0
│       ├── python-dotenv >=0.13
│       ├── pyyaml >=5.1
│       ├── uvloop >=0.14.0,<0.15.0 || >0.15.0,<0.15.1 || >0.15.1
│       ├── watchfiles >=0.13
│       │   └── anyio >=3.0.0
│       │       ├── idna >=2.8
│       │       └── sniffio >=1.1
│       └── websockets >=10.4
├── httpx >=0.23.0
│   ├── anyio *
│   │   ├── idna >=2.8
│   │   └── sniffio >=1.1
│   ├── certifi *
│   ├── httpcore ==1.*
│   │   ├── certifi * (circular dependency aborted here)
│   │   └── h11 >=0.13,<0.15
│   ├── idna * (circular dependency aborted here)
│   └── sniffio * (circular dependency aborted here)
├── jinja2 >=2.11.2
│   └── markupsafe >=2.0
├── orjson >=3.2.1
├── pydantic >=1.7.4,<1.8 || >1.8,<1.8.1 || >1.8.1,<2.0.0 || >2.0.0,<2.0.1 || >2.0.1,<2.1.0 || >2.1.0,<3.0.0
│   ├── annotated-types >=0.4.0
│   ├── pydantic-core 2.18.2
│   │   └── typing-extensions >=4.6.0,<4.7.0 || >4.7.0
│   └── typing-extensions >=4.6.1 (circular dependency aborted here)
├── python-multipart >=0.0.7
├── starlette >=0.37.2,<0.38.0
│   └── anyio >=3.4.0,<5
│       ├── idna >=2.8
│       └── sniffio >=1.1
├── typing-extensions >=4.8.0
├── ujson >=4.0.1,<4.0.2 || >4.0.2,<4.1.0 || >4.1.0,<4.2.0 || >4.2.0,<4.3.0 || >4.3.0,<5.0.0 || >5.0.0,<5.1.0 || >5.1.0
└── uvicorn >=0.12.0
    ├── click >=7.0
    │   └── colorama *
    ├── colorama >=0.4 (circular dependency aborted here)
    ├── h11 >=0.8 
    ├── httptools >=0.5.0
    ├── python-dotenv >=0.13
    ├── pyyaml >=5.1
    ├── uvloop >=0.14.0,<0.15.0 || >0.15.0,<0.15.1 || >0.15.1
    ├── watchfiles >=0.13
    │   └── anyio >=3.0.0
    │       ├── idna >=2.8
    │       └── sniffio >=1.1
    └── websockets >=10.4
fastapi-users 13.0.0 Ready-to-use and customizable users management for FastAPI
├── email-validator >=1.1.0,<2.2
│   ├── dnspython >=2.0.0
│   └── idna >=2.0.0
├── fastapi >=0.65.2
│   ├── email-validator >=2.0.0
│   │   ├── dnspython >=2.0.0
│   │   └── idna >=2.0.0
│   ├── fastapi-cli >=0.0.2
│   │   ├── fastapi * (circular dependency aborted here)
│   │   ├── typer >=0.12.3
│   │   │   ├── click >=8.0.0
│   │   │   │   └── colorama *
│   │   │   ├── rich >=10.11.0
│   │   │   │   ├── markdown-it-py >=2.2.0
│   │   │   │   │   └── mdurl >=0.1,<1.0
│   │   │   │   └── pygments >=2.13.0,<3.0.0
│   │   │   ├── shellingham >=1.3.0
│   │   │   └── typing-extensions >=3.7.4.3
│   │   └── uvicorn >=0.15.0
│   │       ├── click >=7.0 (circular dependency aborted here)
│   │       ├── colorama >=0.4 (circular dependency aborted here)
│   │       ├── h11 >=0.8
│   │       ├── httptools >=0.5.0
│   │       ├── python-dotenv >=0.13
│   │       ├── pyyaml >=5.1
│   │       ├── uvloop >=0.14.0,<0.15.0 || >0.15.0,<0.15.1 || >0.15.1
│   │       ├── watchfiles >=0.13
│   │       │   └── anyio >=3.0.0
│   │       │       ├── idna >=2.8 (circular dependency aborted here)
│   │       │       └── sniffio >=1.1
│   │       └── websockets >=10.4
│   ├── httpx >=0.23.0
│   │   ├── anyio * (circular dependency aborted here)
│   │   ├── certifi *
│   │   ├── httpcore ==1.*
│   │   │   ├── certifi * (circular dependency aborted here)
│   │   │   └── h11 >=0.13,<0.15 (circular dependency aborted here)
│   │   ├── idna * (circular dependency aborted here)
│   │   └── sniffio * (circular dependency aborted here)
│   ├── jinja2 >=2.11.2
│   │   └── markupsafe >=2.0
│   ├── orjson >=3.2.1
│   ├── pydantic >=1.7.4,<1.8 || >1.8,<1.8.1 || >1.8.1,<2.0.0 || >2.0.0,<2.0.1 || >2.0.1,<2.1.0 || >2.1.0,<3.0.0
│   │   ├── annotated-types >=0.4.0
│   │   ├── pydantic-core 2.18.2
│   │   │   └── typing-extensions >=4.6.0,<4.7.0 || >4.7.0 (circular dependency aborted here)
│   │   └── typing-extensions >=4.6.1 (circular dependency aborted here)
│   ├── python-multipart >=0.0.7
│   ├── starlette >=0.37.2,<0.38.0
│   │   └── anyio >=3.4.0,<5 (circular dependency aborted here)
│   ├── typing-extensions >=4.8.0 (circular dependency aborted here)
│   ├── ujson >=4.0.1,<4.0.2 || >4.0.2,<4.1.0 || >4.1.0,<4.2.0 || >4.2.0,<4.3.0 || >4.3.0,<5.0.0 || >5.0.0,<5.1.0 || >5.1.0
│   └── uvicorn >=0.12.0 (circular dependency aborted here)
├── fastapi-users-db-sqlalchemy >=6.0.0
│   ├── fastapi-users >=10.0.0 (circular dependency aborted here)
│   └── sqlalchemy >=2.0.0,<2.1.0
│       ├── greenlet !=0.4.17
│       └── typing-extensions >=4.6.0
├── makefun >=1.11.2,<2.0.0
├── pwdlib 0.2.0
│   ├── argon2-cffi 23.1.0
│   │   └── argon2-cffi-bindings * 
│   │       └── cffi >=1.0.1
│   │           └── pycparser *
│   └── bcrypt 4.1.2
├── pyjwt 2.8.0
│   └── cryptography >=3.4.0
│       └── cffi >=1.12
│           └── pycparser *
└── python-multipart 0.0.9
pydantic 2.7.1 Data validation using Python type hints
├── annotated-types >=0.4.0
├── pydantic-core 2.18.2
│   └── typing-extensions >=4.6.0,<4.7.0 || >4.7.0
└── typing-extensions >=4.6.1
pydantic-settings 2.2.1 Settings management using Pydantic
├── pydantic >=2.3.0
│   ├── annotated-types >=0.4.0
│   ├── pydantic-core 2.18.2
│   │   └── typing-extensions >=4.6.0,<4.7.0 || >4.7.0
│   └── typing-extensions >=4.6.1 (circular dependency aborted here)
└── python-dotenv >=0.21.0
pytest 8.2.0 pytest: simple powerful testing with Python
├── colorama *
├── iniconfig *
├── packaging *
├── httptools >=0.5.0
├── python-dotenv >=0.13
├── pyyaml >=5.1
├── uvloop >=0.14.0,<0.15.0 || >0.15.0,<0.15.1 || >0.15.1
├── watchfiles >=0.13
│   └── anyio >=3.0.0
│       ├── idna >=2.8
│       └── sniffio >=1.1
└── websockets >=10.4
``````
## Структура проекта:
Структура проекта представлена в следующем виде:
``````
cae
├── .pytest_cache
├── .venv
├── docker
│   └── app.sh
├── migrations
│   ├── version
│   ├── env.py
│   └── script.by.mako
├── settings
│   ├── config.py
│   └── .env
├── src
│   ├── auth
│   │   ├── auth.py
│   │   ├── database.py
│   │   ├── manager.py
│   │   └── shemas.py
│   ├── base_models
│   │   ├── meta.py
│   │   └── models.py
│   └── worker
│       └── models.py
├── test
│   ├── auth_test.py
│   └── conf_test.py
├── .env-prod
├── alembic.ini
├── docker-compose.yaml
├── Dockerfile
├── main.py
├── manual.markdown
├──poetry.lock
├──pyproject.toml
└──requirments.txt
``````
Далее будут пояснения о целях и назначении папок / файлов:
- docker - folder - содержит скрипты для докера
- app.sh - file - скрипты для докера
- migrations - folder - дирректория alembic
- versions - folder - содержит миграции для БД
- env.py - file - настройки alembic
- script.by.mako - file - шаблон генерации миграций
- settings - folder - хранит в себе настройки и файл их извлечения
- .env - file - файл настроек БД и ключей для аутентификации
- config.py - file - вытаскивает настройки из предыдущего файла
- test - folder - папка конфигурации тестирования, так же содержит файл тестирования auth
- .env-prod - file - окружение для докер
- alembic.ini - file - файл конфигурации alembic
- docker-compose.ysml - file - сборочный файл докер
- Dockerfile - file - сборка app докера
- main.py - file - старт приложения
- poetry.lock - file - зависимости
- pyproject.toml - file - зависимости
- requirments.txt - file - зависимости
- src - folder - папка основной части приложения
- src/auth - folder - аутентификация приложения
- src/base_models - folder - базовые модели таблиц БД + конечные метаданные
- src/worker - folder - папка "работника"
- src/auth/auth.py - file - файл генерации cookie
- src/auth/database.py - file - точка входа в БД для аутентификации + модель таблицы аутентификации "работника"
- src/auth/manager.py - file - менеджер аутентификации "работника"
- src/base_models/meta.py - file - конечная метадата используемая при генерации миграций
- src/base_models/models.py - file - base модель таблиц
- src/worker/models.py - py - модель таблицы "работника"

## Настройки
- settings/.env - Служит для сборки url БД. Необходимо отредактировать под вашу БД (PostgreSQL - в моем случае). 
- Поля  SECRET_1 и SECRET_2 являются ключами для генерации JWT токена
- settings/config.py - Служит для вытаскивания параметров из .env
- src/auth/auth.py - имеет следующие поля:
``````
  cookie_transport = CookieTransport(cookie_name='shft', cookie_max_age=40)
def get_jwt_strategy() -> JWTStrategy:


    return JWTStrategy(secret=SECRET_1, lifetime_seconds=800)
``````
параметр `cookie_name='shft'` является названием cookie

параметр `cookie_max_age=40` является сроком годности cookie

параметр `lifetime_seconds=800` является временем актуальности cookie
- src/auth/database.py - имеет следующее поле:
``````
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
``````
`postgresql` - БД

`asyncpg` - драйвер для общения с БД

`DB_USER` `DB_PASS` `DB_HOST` `DB_PORT` `DB_NAME`- настройки для БД из settings/.env

- alembic.ini - имеет следующее поле:
``````
sqlalchemy.url = postgresql+asyncpg://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:%(DB_PORT)s/%(DB_NAME)s?async_fallback=True
``````
`postgresql` - БД

`asyncpg` - драйвер для общения с БД

`DB_USER` `DB_PASS` `DB_HOST` `DB_PORT` `DB_NAME`- настройки для БД из settings/.env

`async_fallback=True` - отключение ассинхронности при прогоне миграций (миграции происходят редко, поэтому нет особого смысла включать ассинхронность)

так же в данном файле содержаться следующие строчки:
``````
# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME
``````
представляют из себя включение автоформатера для файлов версий миграции. В моем проекте `black` отключен, но можно их раскоментировать и добавить `black` в виртуальное окружение. Таким образом все созданные файлы миграций будут отформатированы.

# Запуск проекта
После того как проект настроен можно приступать к запуску приложения:
1. Создаём версию миграций для БД командой `alembic revision --autogenerate -m "first_migration"` в терминале.
2. Применим полученную миграцию (можно с помощью `alembic upgrade head`). После этого будет создана таблица "user" в БД.
3. Теперь можно запускать приложение запустив файл main.py (либо вводим в терминал `uvicorn main:app --reload`)

# Работа с эндпоинтами
Документация Swager станет доступна по адресу ``http://127.0.0.1:8000/docs#/`` после запуска приложения.

Всего имеется 5 эндпоинтов:
1. /auth/jwt/login
2. /auth/jwt/logout
3. /auth/register
4. /protected-route-get-data
5. /protected-route-get-salary

Для начала "работнику" надо зарегестрироваться, представим что тем самым он устроился на работу, используем:```/auth/register```

Далее "работнику" надо авторизоваться, используем:```/auth/jwt/login```

Далее "работнику" надо посмотреть текущую ЗП, используем:```protected-roote-get-salary```

Далее "работнику" надо посмотреть дату следующего повышения, используем:```/protected-route-get-data```

После чего работник может разлогиниться, используем:```/auth/jwt/logout```

