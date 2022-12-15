# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import StickerType
from ..base_object import BaseObject


class SearchInstalledStickerSets(BaseObject):
    """
    Searches for installed sticker sets by looking for specified query in their title and name
    
    :param sticker_type: Type of the sticker sets to search for
    :type sticker_type: :class:`StickerType`
    
    :param query: Query to search for
    :type query: :class:`str`
    
    :param limit: The maximum number of sticker sets to return
    :type limit: :class:`int`
    
    """

    ID: str = Field("searchInstalledStickerSets", alias="@type")
    sticker_type: StickerType
    query: str
    limit: int

    @staticmethod
    def read(q: dict) -> SearchInstalledStickerSets:
        return SearchInstalledStickerSets.construct(**q)
