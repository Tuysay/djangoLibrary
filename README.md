   ```
   Source venv/bin/activate
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py collectstatic
   python manage.py test 
   python manage.py createsuperuser
   python manage.py runserver

