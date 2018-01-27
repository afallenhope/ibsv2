class FallenIRC(object):
    def __init__(self, oauth_token=None):
        self._oauth_token = oauth_token
        print("I am a sub class in a package")

    def connect(self):
        print("Connecting please wait...")
