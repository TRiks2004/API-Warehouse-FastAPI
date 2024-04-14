from pydantic_settings import BaseSettings
from sqlalchemy import URL

class FastAPISettings(BaseSettings):
    title: str = "API Warehouse FastAPI" 
    docs_url: str = "/docs"
    debug: bool = True

class PostgresSettings(BaseSettings):
    
    db_name: str = 'warehouse'
    db_host: str = 'warehouse_datebase'
    db_port: int = 5432
    db_user: str = 'postgres'
    db_password: str = 'Bh3AKrv0k45g1R4SbamW'
    db_debug: bool = True

    @property
    def db_url_async(self) -> URL:

        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
        )
    
    
    