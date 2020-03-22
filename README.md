# Knowledge Sharing Platform

To use this project it is recommend it is run in a virtual environment.
This creates an isolated python environment.
Instructions to set up virtual env can be found here: https://virtualenv.pypa.io/en/stable/installation.html

Once in the virtual environment, the user should clone this repository and naviagate to the top level folder.
The user should then run the following command:

```
pip install requirements.txt
```

This installs all the dependencies and packages required for this platform to run.

To run the server, the user should run the following command:

```
python manage.py runserver
```

This will run Django and the platform will be available on the user's computer on the url: ```localhost:8000```