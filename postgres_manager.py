# this module will be imported to other modules
# ------ importing dependencies ------ # 

import psycopg2

# ------ ---------------------- ------ # 

# ------ postgresql important variables ------ #

database_name = 'postgres'
database_user = 'postgres'
auth_password = '91#ABtt5'
host = '127.0.0.1'
port = 5433

# ------ -------------------- ------ #

# ------ postgresql client initialization ------#

connection = psycopg2.connect(dbname = database_name, user = database_user, password = auth_password, host = host, port = port)
connection.autocommit = True
cursor = connection.cursor()

# ------ -------------------------------- ------#