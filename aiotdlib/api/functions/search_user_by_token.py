# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchUserByToken(BaseObject):
    """
    Searches a user by a token from the user's link
    
    :param token: Token to search for
    :type token: :class:`str`
    
    """

    ID: str = Field("searchUserByToken", alias="@type")
    token: str

    @staticmethod
    def read(q: dict) -> SearchUserByToken:
        return SearchUserByToken.construct(**q)
