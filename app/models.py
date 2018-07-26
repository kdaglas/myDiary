import sys
import types


"""  Object classes for the User """


class User(object):

    """ constructor to initialise all params """

    def __init__(self, id, username, emailaddress, password):
        self.id = id
        self.username = username
        self.emailaddress = emailaddress
        self.password = password


class DiaryEntry(types.ModuleType):

    """ constructor to initialise all params """

    def __init__(self, id, title, content, today):
        self.id = id
        self.title = title
        self.content = content
        self.today = today

    def __getitem__(self, key):
        # return self.data["key"]
        pass
