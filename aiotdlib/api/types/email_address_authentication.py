# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class EmailAddressAuthentication(BaseObject):
    """
    Contains authentication data for a email address
    
    """

    ID: str = Field("emailAddressAuthentication", alias="@type")

    
class EmailAddressAuthenticationAppleId(EmailAddressAuthentication):
    """
    An authentication token received through Apple ID
    
    :param token: The token
    :type token: :class:`str`
    
    """

    ID: str = Field("emailAddressAuthenticationAppleId", alias="@type")
    token: str

    @staticmethod
    def read(q: dict) -> EmailAddressAuthenticationAppleId:
        return EmailAddressAuthenticationAppleId.construct(**q)


class EmailAddressAuthenticationCode(EmailAddressAuthentication):
    """
    An authentication code delivered to a user's email address
    
    :param code: The code
    :type code: :class:`str`
    
    """

    ID: str = Field("emailAddressAuthenticationCode", alias="@type")
    code: str

    @staticmethod
    def read(q: dict) -> EmailAddressAuthenticationCode:
        return EmailAddressAuthenticationCode.construct(**q)


class EmailAddressAuthenticationGoogleId(EmailAddressAuthentication):
    """
    An authentication token received through Google ID
    
    :param token: The token
    :type token: :class:`str`
    
    """

    ID: str = Field("emailAddressAuthenticationGoogleId", alias="@type")
    token: str

    @staticmethod
    def read(q: dict) -> EmailAddressAuthenticationGoogleId:
        return EmailAddressAuthenticationGoogleId.construct(**q)

