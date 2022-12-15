# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .file import File
from .sticker import Sticker
from ..base_object import BaseObject


class AnimatedEmoji(BaseObject):
    """
    Describes an animated or custom representation of an emoji
    
    :param sticker: Sticker for the emoji; may be null if yet unknown for a custom emoji. If the sticker is a custom emoji, it can have arbitrary format different from stickerFormatTgs, defaults to None
    :type sticker: :class:`Sticker`, optional
    
    :param sticker_width: Expected width of the sticker, which can be used if the sticker is null
    :type sticker_width: :class:`int`
    
    :param sticker_height: Expected height of the sticker, which can be used if the sticker is null
    :type sticker_height: :class:`int`
    
    :param fitzpatrick_type: Emoji modifier fitzpatrick type; 0-6; 0 if none
    :type fitzpatrick_type: :class:`int`
    
    :param sound: File containing the sound to be played when the sticker is clicked; may be null. The sound is encoded with the Opus codec, and stored inside an OGG container, defaults to None
    :type sound: :class:`File`, optional
    
    """

    ID: str = Field("animatedEmoji", alias="@type")
    sticker: typing.Optional[Sticker] = None
    sticker_width: int
    sticker_height: int
    fitzpatrick_type: int
    sound: typing.Optional[File] = None

    @staticmethod
    def read(q: dict) -> AnimatedEmoji:
        return AnimatedEmoji.construct(**q)
