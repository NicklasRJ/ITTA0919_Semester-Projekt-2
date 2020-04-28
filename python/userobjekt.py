"""
Written by Walther, R.
"""
import datetime


class UserObject():
    """

    """
    def __init__(self, fullname: str, salthash: str):
        """

        """
        self.fullname = fullname
        self.salthash = salthash
        self.creationDate = datetime.datetime.now()