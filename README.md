## lyrics.py
Grab lyrics for any song.

Simply a wrapper around [the api located here](http://api.canarado.xyz), so visit there for more information on the API itself.

This is a simple API to work with.
```py
from lyrics import lyrics

ourSong = lyrics("some arbitrary song name")

if ourSong["status"]["failed"] return print("Bad Response")

print(ourSong["content"][0]["lyrics"])
```