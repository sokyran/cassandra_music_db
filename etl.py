import os
import glob
import csv
import sql_queries as sq
from cassandra.cluster import Cluster

server_ip = '192.168.118.128'
keyspace = 'studentkeyspace'

cluster = Cluster([server_ip])
sess = cluster.connect(keyspace)

"""
Values and dtypes

0. arttist str
1. first_name str
2. gender str
3. item_in_session int 
4. last_name str
5. length float
6. level str
7. location str
8. session_id int 
9. song str
10. user_id int
"""

dtypes = [str, str, str, int, str, float, str, str, int, str, int]
file = 'event_df_new.csv'

def insert_data_to_db(sess, file, query, indices):
	with open(file, encoding='utf8') as f:
		reader = csv.reader(f)
		# skip header row
		next(reader)
		for line in reader:
			values = [dtypes[i](line[i]) for i in indices]
			sess.execute(query, values)


def show_rows(query):
	rows = sess.execute(query);
	for i in rows:
		print(i)
	print('-----------------------------------------------------------------')


# Query 1: Give me the artist, song title and song's length in the music app history 
# that was heard during sessionId = 338, and itemInSession = 4

sess.execute(sq.create_table_art_song_len)
insert_data_to_db(sess, file, sq.insert_into_playlist_asl, [8, 3, 0, 9, 5])
show_rows('select artist, song, length from art_song_len where session_id=338 and item_in_session = 4;')

# Query 2: Give me only the following: 
# name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182

sess.execute(sq.create_table_art_song_user)
insert_data_to_db(sess, file, sq.insert_into_playlist_asu, [10, 8, 0, 9, 3, 1, 4])
show_rows('select artist, song, first_name, last_name from art_song_user where user_id = 10 and session_id = 182;')

# Query 3: Give me every user name (first and last) 
# in my music app history who listened to the song 'All Hands Against His Own'

sess.execute(sq.create_table_user_song)
insert_data_to_db(sess, file, sq.insert_into_playlist_us, [9, 10, 1, 4])
show_rows("select song, first_name, last_name from user_song where song='All Hands Against His Own';")

