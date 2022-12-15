# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class StickerFormat(BaseObject):
    """
    Describes format of a sticker
    
    """

    ID: str = Field("stickerFormat", alias="@type")

    
class StickerFormatTgs(StickerFormat):
    """
    The sticker is an animation in TGS format
    
    """

    ID: str = Field("stickerFormatTgs", alias="@type")

    @staticmethod
    def read(q: dict) -> StickerFormatTgs:
        return StickerFormatTgs.construct(**q)


class StickerFormatWebm(StickerFormat):
    """
    The sticker is a video in WEBM format
    
    """

    ID: str = Field("stickerFormatWebm", alias="@type")

    @staticmethod
    def read(q: dict) -> StickerFormatWebm:
        return StickerFormatWebm.construct(**q)


class StickerFormatWebp(StickerFormat):
    """
    The sticker is an image in WEBP format
    
    """

    ID: str = Field("stickerFormatWebp", alias="@type")

    @staticmethod
    def read(q: dict) -> StickerFormatWebp:
        return StickerFormatWebp.construct(**q)

