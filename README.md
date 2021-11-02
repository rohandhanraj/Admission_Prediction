# Admission_Prediction
Graduate Admission Prediction Model  
**A graduate application is to be completed by a student who wants to enroll in a Master's or doctoral degree. A graduate application will be reviewed by the department that the student applies to along with a Graduate Program Director and/or an admissions committee.**  
**So in this dataset we will predict the Graduate Admissions from an Indian perspective.**

# Commands to run the model on local machine
## Creating a virtual environment for the model
```bash
conda create --prefix ./env python=3.8 -y
```
## Installing the Required Libraries
```bash
pip install -r requirements.txt
```
## Testing the model on localhost
```bash
python predict.py
```

# Commands to build and run the model using Docker container
## Building the Docker image of the Model
```bash
docker image build -t admn-pred .
```
## Running the docker container
```bash
docker run -p 5000:5000 -d admn-pred
```

# Deployment
**Platform: Heroku**
**Code Repo: GitHub**
## Pushing Code to GitHub
```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/rohandhanraj/Admission_Prediction
git push -u origin main
```
## Deploying on Heroku
```bash
heroku login

heroku git:remote -a admn-predixn

git push heroku main
```

# Public Endpoint:
Check the application at: https://admn-predixn.herokuapp.com/
