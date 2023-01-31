# Film Website

**This project is a parser and website about movies. The parser program takes all the movies from the top 250 movies from IMDB.**
##### From third party libraries I have used the following:
```psycopg2``` **(for postgresql)**

```requests``` **(to send http requests)**

```bs4```      **(for parsing data from html markup)**

**(you also need to install PostgreSQL)**

**And for the website, I used the Django framework.**

# Installation and run

**I created a project on Windows, so the commands will be for Windows.**

```pip install psycopg2 psycopg2-binary requests bs4 django```

To run the parser, you just need to go to the appropriate directory and run the ```main.py``` file.
To launch the website, you need to go to the ```movie_site``` directory inside the ```website``` and run this command:

```manage.py runserver --insecure```
