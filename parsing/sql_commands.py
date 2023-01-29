# basic

create_basic_tables = '''CREATE TABLE IF NOT EXISTS film_links (id SERIAL PRIMARY KEY,
																link TEXT, 
															    status BOOLEAN);

						 CREATE TABLE IF NOT EXISTS movies (id SERIAL PRIMARY KEY,
						 									title TEXT,
						 									picture TEXT,
						 									description TEXT,
						 									runtime TEXT,
						 									release_date TEXT,
						 									created_at TEXT);

						CREATE TABLE IF NOT EXISTS director_movies (id SERIAL PRIMARY KEY,
																	director_id INT,
																	movie_id INT);

						CREATE TABLE IF NOT EXISTS actor_movies (id SERIAL PRIMARY KEY,
																 actor_id INT,
																 movie_id INT);

						CREATE TABLE IF NOT EXISTS genre_movies (id SERIAL PRIMARY KEY,
																 genre_id INT,
																 movie_id INT);

						CREATE TABLE IF NOT EXISTS directors (id SERIAL PRIMARY KEY, 
															  name TEXT);

						CREATE TABLE IF NOT EXISTS actors (id SERIAL PRIMARY KEY, 
														   name TEXT);
														   
						CREATE TABLE IF NOT EXISTS genres (id SERIAL PRIMARY KEY,
														   genre TEXT);'''

#######



# ---- insert commands ---- #

# insert table data
insert_movie_data = '''INSERT INTO movies (title, 
										   picture, 
										   description, 
										   runtime, 
										   release_date, 
										   created_at) VALUES ('%s', 
															   '%s', 
															   '%s', 
															   '%s', 
															   '%s', 
															   '%s') RETURNING id'''
insert_director_data = '''INSERT INTO directors (name) VALUES ('%s') RETURNING *;'''
insert_actor_data = '''INSERT INTO actors (name) VALUES ('%s') RETURNING *;'''
insert_genre_data = '''INSERT INTO genres (genre) VALUES ('%s') RETURNING *;'''

# insert bindings
insert_director_movies_data = '''INSERT INTO director_movies (director_id, movie_id) VALUES (%s, %s)'''
insert_actor_movies_data = '''INSERT INTO actor_movies (actor_id, movie_id) VALUES (%s, %s)'''
insert_genre_movies_data = '''INSERT INTO genre_movies (genre_id, movie_id) VALUES (%s, %s)'''

# ---- --------------- ---- #
