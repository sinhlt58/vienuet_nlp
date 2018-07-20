import pygsheets
from mongoengine import connect

class MongoSheet:

    def __init__(self, credential_file):
        self.credential_file = credential_file
        self.gc = pygsheets.authorize(outh_file=credential_file, outh_nonlocal=True)
    