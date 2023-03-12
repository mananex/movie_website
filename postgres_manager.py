# this module will be imported to other modules
# ------ importing dependencies ------ # 

import psycopg2

# ------ ---------------------- ------ # 

# ------ postgresql important variables ------ #

database_name = 'database_name'
database_user = 'database_user'
auth_password = 'auth_password'
host = 'host_ip_adress'
port = 5433 # port

# ------ -------------------- ------ #

# ------ postgresql client initialization ------#

connection = psycopg2.connect(dbname = database_name, user = database_user, password = auth_password, host = host, port = port)
connection.autocommit = True
cursor = connection.cursor()

# ------ -------------------------------- ------#
