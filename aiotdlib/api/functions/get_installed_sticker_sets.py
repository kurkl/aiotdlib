# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import StickerType
from ..base_object import BaseObject


class GetInstalledStickerSets(BaseObject):
    """
    Returns a list of installed sticker sets
    
    :param sticker_type: Type of the sticker sets to return
    :type sticker_type: :class:`StickerType`
    
    """

    ID: str = Field("getInstalledStickerSets", alias="@type")
    sticker_type: StickerType

    @staticmethod
    def read(q: dict) -> GetInstalledStickerSets:
        return GetInstalledStickerSets.construct(**q)
