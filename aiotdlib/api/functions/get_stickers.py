# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import StickerType
from ..base_object import BaseObject


class GetStickers(BaseObject):
    """
    Returns stickers from the installed sticker sets that correspond to a given emoji or can be found by sticker-specific keywords. If the query is non-empty, then favorite, recently used or trending stickers may also be returned
    
    :param sticker_type: Type of the stickers to return
    :type sticker_type: :class:`StickerType`
    
    :param query: Search query; an emoji or a keyword prefix. If empty, returns all known installed stickers
    :type query: :class:`str`
    
    :param limit: The maximum number of stickers to be returned
    :type limit: :class:`int`
    
    :param chat_id: Chat identifier for which to return stickers. Available custom emoji stickers may be different for different chats
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("getStickers", alias="@type")
    sticker_type: StickerType
    query: str
    limit: int
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetStickers:
        return GetStickers.construct(**q)
