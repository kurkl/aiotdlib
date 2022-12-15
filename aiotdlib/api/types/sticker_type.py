# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class StickerType(BaseObject):
    """
    Describes type of a sticker
    
    """

    ID: str = Field("stickerType", alias="@type")

    
class StickerTypeCustomEmoji(StickerType):
    """
    The sticker is a custom emoji to be used inside message text and caption
    
    """

    ID: str = Field("stickerTypeCustomEmoji", alias="@type")

    @staticmethod
    def read(q: dict) -> StickerTypeCustomEmoji:
        return StickerTypeCustomEmoji.construct(**q)


class StickerTypeMask(StickerType):
    """
    The sticker is a mask in WEBP format to be placed on photos or videos
    
    """

    ID: str = Field("stickerTypeMask", alias="@type")

    @staticmethod
    def read(q: dict) -> StickerTypeMask:
        return StickerTypeMask.construct(**q)


class StickerTypeRegular(StickerType):
    """
    The sticker is a regular sticker
    
    """

    ID: str = Field("stickerTypeRegular", alias="@type")

    @staticmethod
    def read(q: dict) -> StickerTypeRegular:
        return StickerTypeRegular.construct(**q)

