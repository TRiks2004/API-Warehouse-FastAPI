## Alembic

> Alembic is a database migration tool that can be used to automate the
> database migration process.
* Создание миграций  
`alembic init <path: генирируемая директория>`

* Выполнение миграции  
`alembic revision --autogenerate -m "message"`

* Закрепление миграции    
`alembic upgrade head`
