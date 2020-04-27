import urllib.request
import urllib.parse
import urllib.error
import json

def lyrics(song_name: str):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}

    req = urllib.request.Request(url="https://api.canarado.xyz/lyrics/" + urllib.parse.quote(song_name), headers=headers)

    with urllib.request.urlopen(req) as res:
        return json.loads(res.read())

print(lyrics("lil darkie black sheep"))