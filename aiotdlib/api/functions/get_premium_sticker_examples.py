# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetPremiumStickerExamples(BaseObject):
    """
    Returns examples of premium stickers for demonstration purposes
    
    """

    ID: str = Field("getPremiumStickerExamples", alias="@type")

    @staticmethod
    def read(q: dict) -> GetPremiumStickerExamples:
        return GetPremiumStickerExamples.construct(**q)
