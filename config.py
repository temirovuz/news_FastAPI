from dotenv import dotenv_values

config = dotenv_values(".env")

DB_USER = config['DB_USER']
DB_PASS = config['DB_PASS']
DB_HOST = config['DB_HOST']
DB_PORT = config['DB_PORT']
DB_NAME = config['DB_NAME']
