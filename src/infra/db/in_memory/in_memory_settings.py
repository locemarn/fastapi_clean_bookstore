from pydantic_settings import BaseSettings, SettingsConfigDict


class InMemorySettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env.test',
        env_file_encoding='utf-8',
        arbitrary_types_allowed=True,
    )

    DATABASE_URL_TEST: str
