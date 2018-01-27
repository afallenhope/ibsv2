# -*- coding: utf-8 -*-
import json
from json import JSONDecodeError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class FallenTwitch(object):
    API_URL = "https://api.twitch.tv/helix/"
    ___client_id = None
    ___client_secret = None
    ___oauth_token = None

    def __init__(self, client_id=None, client_secret=None, oauth_token=None):
        """
        Contructor method

        :param string client_id
        :param string client_secret
        :param string oauth_token
        """
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__oauth_token = oauth_token

    def initialize(self, user=None) -> None:
        """
        Initial cacheing of user/channels information.

        :param str user
        :return None
        """
        print("Initiallized")
        print(self.getFollows(user))

    def getUser(self, user) -> dict:
        """
        Get user details. Mainly used to get the ID
        :param str|int user
        :return dict
        :except JSONDecodeError
        """
        params = {"id": user} if user.isdigit() else {"login": user}
        retVal = self.call_api("/users", params)
        try:
            return json.loads(retVal)
        except JSONDecodeError as err:
            return err

    def get_subscribers(self, uid) -> dict:
        """
        This will be deprecated
        Until official support for subscriptions come into new Api
        Will use this.

        :param int uid
        :returns dict
        :except JSONDecodeErr
        """
        if not uid.isdigit():
            uid = self.getUser(uid)
            uid = uid["data"][0]["id"]

        auth_headers = {
            "Client-ID": self.___client_id,
            "Accept": "application/vnd.twitchtv.v5+json",
            "Authorization": self.___oauth_token
        }
        reqObj = Request("https://api.twitch.tv/kraken/channels/%s/subscriptions" % uid,
                         headers=auth_headers,
                         method="GET")

        with utlopen(reqObj, headers=auth_headers) as response:
            page = response.read()
            try:
                return json.loads(page)
            except JSONDecodeError as err:
                return err


def getFollows(self, uid) -> dict:
    """
    Get users follows, if id is given, gets the user id

    :param int|string
    :returns dict
    :except JSONDecodeError
    """
    if not uid.isdigit():
        uid = self.getUser(uid)
        uid = uid["data"][0]["id"]

    retVal = self.call_api("/users/follows", {"to_id": uid})

    try:
        return json.loads(retVal)
    except JSONDecodeError as err:
        return err


def call_api(self, method, params=None) -> dict:
    """
     Calls API requests to the new Twitch API

    :param string method
    :param dict params
    :return dict
    """
    if params is not None:
        params = urlencode(params)
    req_url = "%s%s?%s" % (self.API_URL, method, params)

    reqObj = Request(req_url, headers={"Client-ID": self.__client_id}, method="GET")
    with urlopen(reqObj) as response:
        page = response.read()
        return page

    return "Invalid Request"
