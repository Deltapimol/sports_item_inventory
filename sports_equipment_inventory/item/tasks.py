import os
import json
import time
import requests
from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task
def fetch_unavailable_items():

    logger.info("Calling fetch unavailable items API")

    url = "http://host.docker.internal:8000/v1/items?available=false"

    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json().get('data', [])

            folder_path = os.path.join("/sports_equipment_inventory/item/", "data_dumps")
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            file_path = os.path.join(folder_path, f"unavailable_items_{int(time.time())}.json")

            logger.info(f"Writing JSON file: {file_path}")

            with open(file_path, 'w') as json_file:
                json.dump(data, json_file)
        except Exception as e:
            logger.error(str(e))
    else:
        logger.error("Error:", response.text)

    logger.info("Task exited")
