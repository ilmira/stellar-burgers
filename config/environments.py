from enum import Enum
from dataclasses import dataclass
from faker import Faker



class Environment(str, Enum):
    DEV = 'dev'
    STAGE = 'stage'

    def __str__(self):
        return {"dev": "DEV", "stage": "STAGE"}[self]

@dataclass
class UserCredentials:
    name: str
    email: str
    password: str

fake = Faker()
common_users = {
    "admin": UserCredentials("Ivan", f"ivantestov{fake.year()}@yandex.ru", "123456"),
    "user": UserCredentials("Pasha", f"pashatestov{fake.year()}@yandex.ru", "123456"),
    "dev_user": UserCredentials("Irin", f"{fake.suffix_female()}{fake.last_name()}{fake.year()}@yandex.ru", "123456"),
    "stage_user": UserCredentials("Kate", f"katetestov{fake.year()}@yandex.ru", "678987")
}

@dataclass
class EnvironmentConfig:
    url: str
    timeout: int
    default_user: str

    def __str__(self):
        return f"- URL: {self.url}"

base_url = "https://stellarburgers.education-services.ru/"

environments = {
    Environment.DEV: EnvironmentConfig(base_url, 15, "dev_user"),
    Environment.STAGE: EnvironmentConfig(base_url, 10, "stage_user")
}

def print_environment_info(env_name, user_type=None):
    """Вывод информации о тестовом окружении."""
    try:
        env = Environment(env_name)
        config = environments[env]
        user_type = user_type or config.default_user
        user = common_users.get(user_type)

        print(f"\nEnvironment: {env}")
        print(f"{config}")

        if user:
            print(f"- User: {user.name}")
        else:
            print(f"- User type '{user_type}' not found!")
    except (ValueError, KeyError):
        print(f"Environment '{env_name}' not found!")
