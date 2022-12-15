# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ClearRecentEmojiStatuses(BaseObject):
    """
    Clears the list of recently used emoji statuses
    
    """

    ID: str = Field("clearRecentEmojiStatuses", alias="@type")

    @staticmethod
    def read(q: dict) -> ClearRecentEmojiStatuses:
        return ClearRecentEmojiStatuses.construct(**q)
