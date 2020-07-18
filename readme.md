This is a repository of Django Geospatial.
System Environment
0. Windows 10
1. Python 3.8
2. PostgreSQL 10
3. Postgis 2.4
4. OSGEO4W. You can download from https://trac.osgeo.org/osgeo4w/

These are steps to run this repository
1. Clone
2. Create virtual environment
    python -m venv virtualenv
    or
    python -m venv virtualenv
3. Install requirements
    pip install -r requirements.txt
    or
    pip3 install -r requirements.txt
4. Run server on geospatial folder that contains manage.py
    python manage.py runserver
    or
    python3 manage.py runserver