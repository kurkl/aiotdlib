# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .input_file import InputFile
from .mask_position import MaskPosition
from .sticker_format import StickerFormat
from ..base_object import BaseObject


class InputSticker(BaseObject):
    """
    A sticker to be added to a sticker set
    
    :param sticker: File with the sticker; must fit in a 512x512 square. For WEBP stickers and masks the file must be in PNG format, which will be converted to WEBP server-side. Otherwise, the file must be local or uploaded within a week. See https://core.telegram.org/animated_stickers#technical-requirements for technical requirements
    :type sticker: :class:`InputFile`
    
    :param emojis: Emojis corresponding to the sticker
    :type emojis: :class:`str`
    
    :param format: Sticker format
    :type format: :class:`StickerFormat`
    
    :param mask_position: Position where the mask is placed; pass null if not specified
    :type mask_position: :class:`MaskPosition`
    
    """

    ID: str = Field("inputSticker", alias="@type")
    sticker: InputFile
    emojis: str
    format: StickerFormat
    mask_position: MaskPosition

    @staticmethod
    def read(q: dict) -> InputSticker:
        return InputSticker.construct(**q)
