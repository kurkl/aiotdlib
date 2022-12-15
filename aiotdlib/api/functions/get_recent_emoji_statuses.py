# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetRecentEmojiStatuses(BaseObject):
    """
    Returns recent emoji statuses
    
    """

    ID: str = Field("getRecentEmojiStatuses", alias="@type")

    @staticmethod
    def read(q: dict) -> GetRecentEmojiStatuses:
        return GetRecentEmojiStatuses.construct(**q)
