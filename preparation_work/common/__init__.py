from .settings import FastAPISettings, PostgresSettings

class Settings():

    

    @property
    def fastapi(self) -> dict:
        return FastAPISettings().model_dump()

    @property
    def postgres(self) -> dict:
        settings_database = PostgresSettings()
        return {
            'url': settings_database.db_url_async,
            'echo': settings_database.db_debug
        }

