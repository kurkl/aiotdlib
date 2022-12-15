# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import StickerType
from ..base_object import BaseObject


class GetArchivedStickerSets(BaseObject):
    """
    Returns a list of archived sticker sets
    
    :param sticker_type: Type of the sticker sets to return
    :type sticker_type: :class:`StickerType`
    
    :param offset_sticker_set_id: Identifier of the sticker set from which to return the result
    :type offset_sticker_set_id: :class:`int`
    
    :param limit: The maximum number of sticker sets to return; up to 100
    :type limit: :class:`int`
    
    """

    ID: str = Field("getArchivedStickerSets", alias="@type")
    sticker_type: StickerType
    offset_sticker_set_id: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetArchivedStickerSets:
        return GetArchivedStickerSets.construct(**q)
