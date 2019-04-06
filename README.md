**How to run this project**
Docker and docker compose are requiered in order to run this small django sample project.
Steps to run the service:
* Enter in the container:
```bash
sudo docker-compose run web bash
```
* Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
* Up the Api
```bash
```
* Create a bank
Follow the address http://localhost:8000/bancos/add_banco/ and create your bank!

**To create a new project run:**
```bash 
sudo docker-compose run web django-admin.py startproject app_name .
```

**To connect directly in the db you can use one of the next commands:**
```python manage.py dbshell```
```sudo docker run -it --rm --link djangoapp_postgres_1:postgres --net djangoapp_default postgres psql -h postgres -U postgres```

# REFERENCES:
* [quickstart compose and django](https://docs.docker.com/compose/django/#connect-the-database)
* [postgres doc](https://hub.docker.com/_/postgres/)
