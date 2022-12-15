# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetUserLink(BaseObject):
    """
    Returns an HTTPS link, which can be used to get information about the current user
    
    """

    ID: str = Field("getUserLink", alias="@type")

    @staticmethod
    def read(q: dict) -> GetUserLink:
        return GetUserLink.construct(**q)
