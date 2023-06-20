# Install venv

python -m venv .myvenv

# Activate venv

myvenv\Scripts\activate

# Run server

py manage.py runserver

# Migrate server to update new changes to the model

py manage.py makemigrations 'your app's model'

# After updating the model successfully, run the migration

py manage.py migrate

# Open Python shell

py manage.py shell
