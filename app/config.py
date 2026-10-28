from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Beacon API"
    app_env: str = "development"
    secret_key: str
    database_url: str = "sqlite:///./app.db"
    cors_origins: str = "http://localhost:5173"

    @property
    def origin_list(self) -> list[str]:
        return [item.strip() for item in self.cors_origins.split(",") if item.strip()]


settings = Settings()
