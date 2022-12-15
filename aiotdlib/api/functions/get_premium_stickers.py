# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetPremiumStickers(BaseObject):
    """
    Returns premium stickers from regular sticker sets
    
    :param limit: The maximum number of stickers to be returned; 0-100
    :type limit: :class:`int`
    
    """

    ID: str = Field("getPremiumStickers", alias="@type")
    limit: int

    @staticmethod
    def read(q: dict) -> GetPremiumStickers:
        return GetPremiumStickers.construct(**q)
