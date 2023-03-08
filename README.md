# Film website

## This is a project to parse the top 250 movies from IMDB and display it on a website using the Django framework.

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

