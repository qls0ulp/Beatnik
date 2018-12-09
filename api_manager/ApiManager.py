import logging
import os
import spotipy
import sys

from gmusicapi import Mobileclient
from spotipy.oauth2 import SpotifyClientCredentials

from . import LinkConverter
from . import LinkParser
from . import SearchHandler
from apple_music_api import AppleMusicApi
from soundcloud_api import SoundcloudApi

class ApiManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.apple_api = self.get_apple_api()
        self.gpm_api = self.get_gpm_api()
        self.soundcloud_api = self.get_soundcloud_api()
        self.spotify_api = self.get_spotify_api()
        self.link_parser = LinkParser.LinkParser(
                self.apple_api,
                self.gpm_api,
                self.soundcloud_api,
                self.spotify_api)
        self.link_converter = LinkConverter.LinkConverter(
                self.apple_api,
                self.gpm_api,
                self.soundcloud_api,
                self.spotify_api,
                self.link_parser)
        self.search_handler = SearchHandler.SearchHandler(self.spotify_api, self.link_converter)

    def get_apple_api(self):
        key_id = os.environ['APPLE_KEY_ID']
        issuer = os.environ['APPLE_KEY_ISSUER']
        key = os.environ['APPLE_KEY']
        return AppleMusicApi.AppleMusicApi(key_id=key_id,
                issuer=issuer,
                key=key)

    def get_gpm_api(self):
        gpm_api = Mobileclient()
        username = os.environ['GPM_USERNAME']
        password = os.environ['GPM_PASSWORD']

        if (not gpm_api.login(username, password, Mobileclient.FROM_MAC_ADDRESS, 'en_US')):
            self.logger.error("Unable to login to Google Play Music.")
            return None

        return gpm_api

    def get_soundcloud_api(self):
        return SoundcloudApi.SoundcloudApi()

    def get_spotify_api(self):
        client_credentials_manager = SpotifyClientCredentials()
        return spotipy.Spotify(client_credentials_manager=client_credentials_manager)
