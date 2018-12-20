'''
Preprocess MPD's data into models
'''
import os, json
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors


def set_data(dataset):
    all_playlists = {}
    all_tracks = {}
    all_artists = {}

    for playlist in dataset:
        pid = playlist['pid']
        all_playlists[pid] = playlist

    playlists_arr = all_playlists.values()
    for playlist in playlists_arr:
        tracks = playlist['tracks']
        for track in tracks:
            track_uri = track['track_uri']
            artist_uri = track['artist_uri']
            all_tracks[track_uri] = track
            
            if all_artists.__contains__(artist_uri):
                all_artists[artist_uri].add(track['album_uri'])
            else:
                all_artists[artist_uri] = set([track['album_uri']])

        # all_playlists is {'pid_val': playlist}
        # all_tracks is {'track_uri_val': track}
        # all_artists is {'artist_uri_val': artist}

    return [all_playlists, all_tracks, all_artists]

def preprocess(test_size=0.2):
    
    path_to_json = 'data/'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    data = []
    for idx, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as js_file:
            new_data = json.load(js_file)
            data += new_data['playlists']

    # split train/test json in 80/20
    train_json, test_json = train_test_split(data, test_size = test_size)

    # transfer json into dataframe
    train_set = json_normalize(train_json, 'tracks', ["name", "collaborative", "pid", "modified_at", "num_tracks", "num_albums", "num_followers"], record_prefix='tracks_')
    test_set = json_normalize(test_json, 'tracks', ["name", "collaborative", "pid", "modified_at", "num_tracks", "num_albums", "num_followers"], record_prefix='tracks_')

    # print intermediate parameters like the size of train_set and test_set, the amounts of both datasets.
    result = 'Correct' if len(train_set) + len(test_set) == 266386 else 'Incorrect'
    print('Data preprocess starts.')
    print(f'This train_set has {str(len(train_json))} playlists with {str(len(train_set))} tracks and test_set has {str(len(test_json))} playlists with {str(len(test_set))} tracks.')
    print(f'Data size for both train_set and test_set are {result} as they sum up to 266386 in total.')
    print('Data preprocess ends.')
    print('______________________')

    df_train_set = train_set.drop(['tracks_pos', 'modified_at'], axis=1)
    df_test_set = test_set.drop(['tracks_pos', 'modified_at'], axis=1)

    # generate values of tracks_track_name
    # print(list(df.tracks_track_name.values))

    # all sorted unique pid value
    # print((df_train_set.sort_values(by=['pid'])['pid']).unique())

    # generate data which pid=12
    # print(df[df.pid==12][['tracks_track_name', 'tracks_pos']])

    # make sure there is no missing value
    # print(df_train_set.isnull().sum())

    return [df_train_set, df_test_set]

def df_matrix(train_set, test_size=0.2):
    # tracks_by_popularity is track_uri numpy.ndarray with descending order of popularity, need refactor
    tracks_by_popularity = train_set[['tracks_track_uri','pid']].groupby([ 'tracks_track_uri'])['pid'].count().reset_index(name='count').sort_values(['count'], ascending=False)

    tracks_dict_by_popularity = { v: index for index, v in np.ndenumerate(tracks_by_popularity)}

    print('df_matrix intermediate results')

    # hard-code dataset size
    playlist_track_matrix = np.zeros(shape=(int(4000*(1-test_size)),len(train_set)))

    
    # print(tracks_dict_by_popularity.values())
    print(playlist_track_matrix.shape)
    print('================')



# from sklearn.neighbors import NearestNeighbors


print('Test starts.')
print('_____________________')
[train_set, test_set] = preprocess()
train_lst = df_matrix(train_set)

print('Test ends.')
print('_____________________')
# test_lst = df_matrix(test_set)
# any_pid = (test_set.sort_values(by=['pid'])['pid']).unique()[0]
# print('pid is ' + str(any_pid))

# fetch values by key
# print(test_set[test_set.pid==any_pid].sum())
# print(real_result)
# neigh = NearestNeighbors()

# all_set = pd.concat([train_set, test_set])

# ## fetch all distinct track count in all_set
# # print((all_set['tracks_track_uri'].nunique()))

# # most popular tracks
# popular_set = all_set[['tracks_track_uri','pid', 'tracks_track_name']].groupby(['tracks_track_name', 'tracks_track_uri'])['pid'].count().reset_index(name='count').sort_values(['count'], ascending=False)
# popular_set['count %'] = popular_set.apply(lambda row: row['count']/4000*100, axis=1)

# print(popular_set.head(10))

