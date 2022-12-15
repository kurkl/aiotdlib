# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import StickerType
from ..base_object import BaseObject


class GetTrendingStickerSets(BaseObject):
    """
    Returns a list of trending sticker sets. For optimal performance, the number of returned sticker sets is chosen by TDLib
    
    :param sticker_type: Type of the sticker sets to return
    :type sticker_type: :class:`StickerType`
    
    :param offset: The offset from which to return the sticker sets; must be non-negative
    :type offset: :class:`int`
    
    :param limit: The maximum number of sticker sets to be returned; up to 100. For optimal performance, the number of returned sticker sets is chosen by TDLib and can be smaller than the specified limit, even if the end of the list has not been reached
    :type limit: :class:`int`
    
    """

    ID: str = Field("getTrendingStickerSets", alias="@type")
    sticker_type: StickerType
    offset: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetTrendingStickerSets:
        return GetTrendingStickerSets.construct(**q)
