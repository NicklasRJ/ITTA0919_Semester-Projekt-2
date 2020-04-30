"""
Written by Walther, R.
"""
import datetime
import random
import string


class UserObject:
    """Represents an user with fullname, assigned pincode in salthashed form
    and various other unique, identifiable variables.

    Supported operators:
    
    TODO: Add some!

    Methods:

    GenerateIdString()

    Properties (readonly):

    fullname, userId, salthash
    """
    def __init__(self, fullname: str, salthash: str):
        """Constructer

        Arguments:
        fullname -- The fullname of the user in string format.
        salthash -- Salthashed pincode in string format assigned to the user. 
        """
        if not isinstance(fullname, str):
            raise TypeError(fullname)
        if not isinstance(salthash, str):
            raise TypeError(salthash)

        self._fullname       = fullname
        self._userId         = self.GenerateIdString()
        self._salthash       = salthash
        self._creationDate   = datetime.datetime.now()
    
    def GenerateIdString(self, length=8) -> str:
        """Returns a string containing random alpha and numeric characters.
        
        Arguments:
        length -- the length of the string in characters (default = 8).
        """
        if not isinstance(length, int):
            raise ValueError(length)
        characters = string.ascii_letters + string.digits
        return "".join((random.choice(characters) for _ in range(length)))


test = UserObject("test","test")