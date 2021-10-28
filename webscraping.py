from bs4 import BeautifulSoup as soup
import requests
import json
import logging
import sys
from http.client import HTTPConnection
import exceptions



# class for webscraping
class scrape:
    song_url = 'https://gaana.com/songs'

    def connectToURL(self):

        # HTTPConnection.debuglevel = 1

        formatter = logging.Formatter('%(asctime)s , %(filename)s , %(name)s ,  %(levelname)s , %(message)s')

        file_handler = logging.FileHandler('errorlog.log')
        file_handler.setFormatter(formatter)

        connection_handler = logging.getLogger('urllib3.connectionpool')
        connection_handler.setLevel(logging.DEBUG)
        connection_handler.addHandler(file_handler)

        print('connection to song url')
        songs_status = requests.get(self.song_url)

        print("songs_status: ",songs_status)

        if (songs_status.status_code != 200):
            raise exceptions.connection_error("unable to connect to Source site : https://gaana.com/songs")
            # raise Exception("unable to connect to Source site : https://gaana.com/songs")
        # print(type("song status type : ",song_status))
        songs_data = requests.get(self.song_url).text

        songs_soup = soup(songs_data, 'html.parser')

        songs_list = songs_soup.findAll('ul', {'class': '_row list_data'})
        songs_text = []
        for song in songs_list:
            songs_text.append([data.text.strip() for data in song.findAll('span', {})])
        # print(songs_text)

        list_heading = songs_soup.find('ul', {'class': '_row list_heading sm-hide'})
        col1 = [data.text for data in list_heading.findAll('span', {})][1:]
        # print(col1)

        song_data = []

        for item in songs_text:
            each_song = {}
            for index, song in enumerate(item):
                each_song[col1[index]] = song

            song_data.append(each_song)

        # print(song_data)

        filename = 'trending.json'

        with open(filename, 'w') as f:
            json_data = json.dumps(song_data,indent=1)
            json.dump(song_data, f, indent=1)
