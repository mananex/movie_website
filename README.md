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

<b>Note:</b> all SQL requests are made using the ```postgres_manager.py``` module, which is common for both the parser and the website.

#### Step 3. Installing important modules.

Now you need to use pip to install all the necessary modules for the project to work correctly (the parser and the site itself).<br/>
All required modules are written in the ```requirements.txt``` file.<br/>

To install them, enter the command ```pip install -r requirements.txt``` in the <b>terminal / command line</b>.

<hr>

### The parser program.

The parsing program is needed, oddly enough, to parse the films themselves from IMDB.<br/>
The ```sql_commands.py``` file contains the main SQL queries to the server.

### ―――――――――――

To start the parser, you first need to start pgAdmin, then start the server itself, with which the parser program will interact.
After that, you need to run the ```main.py``` file to start parsing pages. Command: ```python main.py```.

### ―――――――――――

As the parser works, the data will be written to the appropriate tables in the database. You can see which tables will be created in the ```parsing\sql_commands.py``` file in the ```create_basic_tables``` variable, which contains commands to the server to create basic tables.

<hr>

### The website.

To run a website, you must first start pgAdmin, start the server where the parsed data is located.<br/>
After that, you need to go to the ```website/movie_site``` directory and run the ```manage.py``` program.<br/>
Running the script must be done through the <b>terminal/command line</b> using the following command: ```python manage.py runserver --insecure```.

<hr>
