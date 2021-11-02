#FROM python:3.8-slim-buster

#COPY requiremets.txt .

#RUN pip install -r requiremets.txt

#COPY . .

#ENV FLASK_APP  predict.py
#EXPOSE 9089
#CMD ["flask", "run", "--host=0.0.0.0", "--port=9089"]

# Base Image
#FROM python:3.8-slim-buster

# Define the present working directory
#WORKDIR /app
# Add all the files to the present working directory
#COPY . /app
# Install pip requirements
#RUN pip install -r requirements.txt

# Expose the port
#EXPOSE 8001
#CMD [ "python", "predict.py" ]
#ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:8001", "predict:app" ]

FROM python:3.8.12-slim

#RUN pip install pipenv

WORKDIR /app

#COPY ["Pipfile", "Pipfile.lock", "./"]

#RUN pipenv install --system --deploy

COPY . .

RUN pip install -r requirements.txt

EXPOSE 9089

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9089", "predict:app"]