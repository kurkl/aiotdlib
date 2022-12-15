# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetCustomEmojiStickers(BaseObject):
    """
    Returns list of custom emoji stickers by their identifiers. Stickers are returned in arbitrary order. Only found stickers are returned
    
    :param custom_emoji_ids: Identifiers of custom emoji stickers. At most 200 custom emoji stickers can be received simultaneously
    :type custom_emoji_ids: :class:`list[int]`
    
    """

    ID: str = Field("getCustomEmojiStickers", alias="@type")
    custom_emoji_ids: list[int]

    @staticmethod
    def read(q: dict) -> GetCustomEmojiStickers:
        return GetCustomEmojiStickers.construct(**q)
