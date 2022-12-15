# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetCustomEmojiReactionAnimations(BaseObject):
    """
    Returns TGS stickers with generic animations for custom emoji reactions
    
    """

    ID: str = Field("getCustomEmojiReactionAnimations", alias="@type")

    @staticmethod
    def read(q: dict) -> GetCustomEmojiReactionAnimations:
        return GetCustomEmojiReactionAnimations.construct(**q)
