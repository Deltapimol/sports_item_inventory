
## Environment File

Create a '.env' file using the 'env.sample' file as reference

## Commands

### Run project

```sh
docker-compose up --build
```

### Create superuser

```sh
docker exec -it <django_app container id> python manage.py createsuperuser
```

## Postman API collection

Import the Postman collection JSON file from the project in the Postman client to test APIs


## Celery Job

The Celery container will execute a job to call the API to fetch unavailable items every minute. This task also writes a new JSON file in *`sports_item_inventory/item/data_dumps`* directory
The frequency of this job can be altered through the crontab function in `CELERY_BEAT_SCHEDULE` in Settings.py
