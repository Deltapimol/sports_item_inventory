## Commands

### Run project

```sh
docker-compose up --build
```

### Create superuser

```sh
docker exec -it <django_app container id> python manage.py createsuperuser
```
