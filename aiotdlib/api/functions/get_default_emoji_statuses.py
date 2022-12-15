# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetDefaultEmojiStatuses(BaseObject):
    """
    Returns default emoji statuses
    
    """

    ID: str = Field("getDefaultEmojiStatuses", alias="@type")

    @staticmethod
    def read(q: dict) -> GetDefaultEmojiStatuses:
        return GetDefaultEmojiStatuses.construct(**q)
