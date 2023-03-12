# Film website

## This is a project to parse the top 250 movies from IMDB and display it on a website using the Django framework.

<hr>

### General steps.
#### Step 1. Installing important tools.

You need to install Python on your computer first. I am using Python 3.7.9.<br/>
After that, you need to install pgAdmin to run the PostgreSQL server.

#### Step 2. Setting options.

To set options, you need to open the ```postgres_manager.py``` file, and set the required options there in the appropriate variables.

```database_name``` - database name<br/>
```database_user``` - postgresql user<br/>
```auth_password``` - authentication password<br/>
```host``` - ip adress (you can set 127.0.0.1)<br/>
```port``` - server port (default is 5432)<br/>

<hr>

### The parser program.

The parsing program is needed, oddly enough, to parse the films themselves from IMDB.

The ```sql_commands.py``` file contains the main SQL queries to the server.

<b>Note:</b> all SQL requests are made using the ```postgres_manager.py``` module, which is common for both the parser and the website.

### ―――――――――――

For the parser, I use the following tools:

```psycopg2``` ┋ For PostgreSQL.<br/>
```requests``` ┋ To send GET requests.<br/>
```beautifulsoup4``` ┋ For parsing data from html.<br/>
```random_user_agent``` ┋ For random user agents to send GET requests.

### ―――――――――――





