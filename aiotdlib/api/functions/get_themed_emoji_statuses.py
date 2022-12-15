# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetThemedEmojiStatuses(BaseObject):
    """
    Returns up to 8 themed emoji statuses, which color must be changed to the color of the Telegram Premium badge
    
    """

    ID: str = Field("getThemedEmojiStatuses", alias="@type")

    @staticmethod
    def read(q: dict) -> GetThemedEmojiStatuses:
        return GetThemedEmojiStatuses.construct(**q)
