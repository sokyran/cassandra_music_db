create_table_art_song_len = """
	CREATE TABLE IF NOT EXISTS art_song_len(
		session_id int,
		item_in_session int,
		artist text,
		song text,
		length float,
		PRIMARY KEY(session_id, item_in_session)
	);
"""


insert_into_playlist_asl = """
	INSERT INTO art_song_len(
		session_id, item_in_session, artist, song, length)
	VALUES (%s, %s, %s, %s, %s);
"""


create_table_art_song_user = """
	CREATE TABLE IF NOT EXISTS art_song_user(
		user_id int,
		session_id int,
		artist text,
		song text,
		item_in_session int,
		first_name text,
		last_name text,
		PRIMARY KEY ((user_id, session_id), item_in_session)
	);
"""


insert_into_playlist_asu = """
	INSERT INTO art_song_user(
		user_id, session_id, artist, song, item_in_session, first_name, last_name
	) VALUES (
		%s, %s, %s, %s, %s, %s, %s
	);
"""


create_table_user_song = """
	CREATE TABLE IF NOT EXISTS user_song(
		song text,
		user_id int,
		first_name text,
		last_name text,
		PRIMARY KEY(song, user_id)
		);
"""


insert_into_playlist_us = """
	INSERT INTO user_song(
		song, user_id, first_name, last_name
	) VALUES (
		%s, %s, %s, %s
	);
"""