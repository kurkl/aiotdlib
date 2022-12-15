# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class UserLink(BaseObject):
    """
    Contains an HTTPS URL, which can be used to get information about a user
    
    :param url: The URL
    :type url: :class:`str`
    
    :param expires_in: Left time for which the link is valid, in seconds; 0 if the link is a public username link
    :type expires_in: :class:`int`
    
    """

    ID: str = Field("userLink", alias="@type")
    url: str
    expires_in: int

    @staticmethod
    def read(q: dict) -> UserLink:
        return UserLink.construct(**q)
