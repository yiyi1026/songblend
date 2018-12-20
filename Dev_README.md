
## Preparation period - 5 ~ 7 days
-------

### Recommendation system algorithms - 3 ~ 5 days
============================

- model type
  collaborative filter 
  1. user-based
    no information about user profile.
  2. item-based
    playlists: playlist_title, track(track_title, artist_name,album_title),

what are the inputs?
  user-created playlists
what are the outputs?
  new playlists (about 30 songs, no duplicates, no seeds from inputs, order matters)

- GAN or not?
probably not yet
- dataset decision

- should I check for dataset internal consistency before training?

  Yes

- does track position mean anything? Should I store this information in dataset?

- what does similarity mean? 
  1. cosine similarity of different length 
      row in playlists, column in songs
      for playlist-playlist similarity, row is the vector
      for song-song similarity, column is the vector
  2. does order matter?

 use pandas library to read data.
 but how to store the mid-state model result??

### Dataset Preparation Period - 1 ~ 2 days
============================
- [x] import data from json files
- [x] remove duplicate, incorrect data
- [x] build database

## Coding period - 7 ~ 9 days
- [x] build similarity functions
- [ ] build training model
-------------

### Algorithms Coding/ Model Training Period - 3 ~ 5 days
===============
- small-size data 
- commercial size data 

### UI period - 1 ~ 2 days
============================
- [ ]  user interface build & decoration period
- [ ]  input 
- [ ]  output playlists( >= 10 songs)

### spotify API - 1 ~ 2 days
============================








