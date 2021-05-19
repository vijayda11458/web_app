import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'helloworld12356.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacity-excercise'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'UDACITYstudent1'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacitystorage1'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'h7R9M/fjm0FX9WGrJBujhV4DOJdecZbTn0PJaIjvSFlyk8nwbhJ8l0zh1Y/vL+ANcTAaH2jyw2BprTu47Ohzmw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
