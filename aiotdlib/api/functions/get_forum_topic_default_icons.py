# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetForumTopicDefaultIcons(BaseObject):
    """
    Returns list of custom emojis, which can be used as forum topic icon by all users
    
    """

    ID: str = Field("getForumTopicDefaultIcons", alias="@type")

    @staticmethod
    def read(q: dict) -> GetForumTopicDefaultIcons:
        return GetForumTopicDefaultIcons.construct(**q)
