# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .closed_vector_path import ClosedVectorPath
from .file import File
from .mask_position import MaskPosition
from .sticker_format import StickerFormat
from .sticker_type import StickerType
from .thumbnail import Thumbnail
from ..base_object import BaseObject


class Sticker(BaseObject):
    """
    Describes a sticker
    
    :param set_id: The identifier of the sticker set to which the sticker belongs; 0 if none
    :type set_id: :class:`int`
    
    :param width: Sticker width; as defined by the sender
    :type width: :class:`int`
    
    :param height: Sticker height; as defined by the sender
    :type height: :class:`int`
    
    :param emoji: Emoji corresponding to the sticker
    :type emoji: :class:`str`
    
    :param format: Sticker format
    :type format: :class:`StickerFormat`
    
    :param type_: Sticker type
    :type type_: :class:`StickerType`
    
    :param mask_position: Position where the mask is placed; may be null even the sticker is a mask, defaults to None
    :type mask_position: :class:`MaskPosition`, optional
    
    :param custom_emoji_id: Identifier of the emoji if the sticker is a custom emoji
    :type custom_emoji_id: :class:`int`
    
    :param outline: Sticker's outline represented as a list of closed vector paths; may be empty. The coordinate system origin is in the upper-left corner
    :type outline: :class:`list[ClosedVectorPath]`
    
    :param thumbnail: Sticker thumbnail in WEBP or JPEG format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    
    :param is_premium: True, if only Premium users can use the sticker
    :type is_premium: :class:`bool`
    
    :param premium_animation: Premium animation of the sticker; may be null, defaults to None
    :type premium_animation: :class:`File`, optional
    
    :param sticker: File containing the sticker
    :type sticker: :class:`File`
    
    """

    ID: str = Field("sticker", alias="@type")
    set_id: int
    width: int
    height: int
    emoji: str
    format: StickerFormat
    type_: StickerType = Field(..., alias='type')
    mask_position: typing.Optional[MaskPosition] = None
    custom_emoji_id: int
    outline: list[ClosedVectorPath]
    thumbnail: typing.Optional[Thumbnail] = None
    is_premium: bool
    premium_animation: typing.Optional[File] = None
    sticker: File

    @staticmethod
    def read(q: dict) -> Sticker:
        return Sticker.construct(**q)
