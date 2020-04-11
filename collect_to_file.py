import os
import glob
import pandas as pd
from datetime import datetime

root = 'event_data'
files = glob.glob(os.path.join(root, '*.csv'))


cols_to_save = ['artist', 'firstName', 'gender', 'itemInSession', 'lastName',
				'length', 'level', 'location', 'sessionId', 'song', 'userId']

new_cols = ['artist', 'first_name', 'gender', 'item_in_session', 'last_name',
				'length', 'level', 'location', 'session_id', 'song', 'user_id']

full_df = pd.DataFrame()
for f in files:
	sm_df = pd.read_csv(f)
	full_df = full_df.append(sm_df[sm_df['artist'].notna()])
	
full_df['ts'].apply(lambda x: datetime.fromtimestamp(x/1000.0))
full_df = full_df[cols_to_save]
full_df.columns = new_cols
full_df['user_id'] = full_df['user_id'].astype(int)
full_df.to_csv('event_df_new.csv', index=False)





