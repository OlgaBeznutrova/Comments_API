## Comments API 

:white_check_mark: FastAPI with Django ORM   

#### Python 3.9
####PostrgeSQL


### Directory hierarchy
![img.png](img.png)
!(https://drive.google.com/file/d/1odBRSS3YLKJQLzZxnKy66_cS69l9Dzv9/view?usp=sharing)

* **models**: Django models
* **urls**: FastAPI routers
* **schemas**: Pydantic models
* **db_service**: database context
____
### Required environment variables:

* **FST_HOST** - Fastapi host _# default "0.0.0.0"_
* **FST_PORT** - Fastapi port _# default 8000_
* **DB_NAME** - database name
* **DB_USER** - database user
* **DB_PASSWORD** - database password
* **DB_HOST** - database host _# default "localhost"_
* **DB_PORT** - database port _# default "5432"_

_____
### Migration before the run
python manage.py migrate
_____

### Run
**python main.py** _# FastApi_

for example: http://127.0.0.1:8000/docs#/ _# Swagger UI_

**python manage.py runserver 0.0.0.0:9000** _# Django_

for example: http://127.0.0.1:9000/admin/ _# Admin panel_
_____

Dependencies are listed in **requirements.txt**

