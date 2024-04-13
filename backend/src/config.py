from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    smtp_host: str
    smtp_port: int
    smtp_username: str
    smtp_password: str
    backend_api_url: str

    class Config:
        env_file = ".env"


settings = Settings()
