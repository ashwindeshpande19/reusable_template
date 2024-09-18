Reusable Template
Overview
This Django project provides a template to generate custom images using the Renderform API.

Features
Form Submission: Collects data through a Django form.
API Integration: Sends data to the Renderform API to generate custom images given the template.

Prerequisites
Make sure you have the following installed:

Python 3.10

pip: The package installer for Python.

Conda (Optional): To manage Python environments (you can use virtualenv or other virtual environment managers).

Renderform API Key: You will need a valid API key from Renderform.

Insert your api key in the views.py file where api_key = 'YOUR_API_KEY'

Installation Steps

1)Clone the repository

2)Go in the folder where the repository is cloned

2)Install Dependencies

pip install -r requirements.txt

3)Apply Migrations

python manage.py migrate

4)Run the Development Server

python manage.py runserver