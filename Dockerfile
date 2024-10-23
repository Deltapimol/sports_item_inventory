FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /sports_equipment_inventory

COPY requirements.txt /sports_equipment_inventory/

RUN pip install -r requirements.txt

COPY ./sports_equipment_inventory /sports_equipment_inventory

EXPOSE 8000