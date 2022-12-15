# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import StickerType
from ..base_object import BaseObject


class ReorderInstalledStickerSets(BaseObject):
    """
    Changes the order of installed sticker sets
    
    :param sticker_type: Type of the sticker sets to reorder
    :type sticker_type: :class:`StickerType`
    
    :param sticker_set_ids: Identifiers of installed sticker sets in the new correct order
    :type sticker_set_ids: :class:`list[int]`
    
    """

    ID: str = Field("reorderInstalledStickerSets", alias="@type")
    sticker_type: StickerType
    sticker_set_ids: list[int]

    @staticmethod
    def read(q: dict) -> ReorderInstalledStickerSets:
        return ReorderInstalledStickerSets.construct(**q)
