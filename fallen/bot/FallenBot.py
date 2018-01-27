# -*- coding: utf-8 -*-
from fallen.db import FallenDB
from fallen.irc import FallenIRC
from fallen.twitch import FallenTwitch


class FallenBot:
    settings = {}

    def __init__(self, client_id=None, client_secret=None, oauth_token=None):
        """
        Contructor method
        :param string client_id
        :param string client_secret
        :param string oauth_token
        """
        # self.thread_Twitch = None
        # self.thread_IRC = None
        __db = FallenDB.FallenDB("config/fallendb.db")

        self.settings['twitch_client_id'] = __db.get_setting("twitch_client_id")
        self.settings['twitch_client_secret'] = __db.get_setting('twitch_client_secret')
        self.settings['twitch_token'] = __db.get_setting('twitch_token')

        self.client_id = self.settings['twitch_client_id'][2] if self.settings[
                                                                     'twitch_client_id'] is not None else client_id
        self.client_secret = self.settings['twitch_client_secret'][2] if self.settings[
                                                                             'twitch_client_secret'] is not None else client_secret
        self.oauth_token = self.settings['twitch_token'][2] if self.settings[
                                                                   'twitch_token'] is not None else oauth_token

        self.TwitchClient = FallenTwitch.FallenTwitch(self.client_id)
        self.IRCClient = FallenIRC.FallenIRC()

    def start_twitchclient(self, user):
        """
        Starts the twitch client

        :param string user
        :return None
        """
        # self.thread_Twitch = threading.Thread(target=self.fallenTwitch.connect())
        # self.thread_IRC = threading.Thread(target=self.fallenIRC.initialize())
        # self.thread_Twitch.start()
        # self.thread_IRC.start()
        self.TwitchClient.initialize(user)
        print(self.TwitchClient.getUser(""))
