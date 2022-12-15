# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ReactionType(BaseObject):
    """
    Describes type of message reaction
    
    """

    ID: str = Field("reactionType", alias="@type")

    
class ReactionTypeCustomEmoji(ReactionType):
    """
    A reaction with a custom emoji
    
    :param custom_emoji_id: Unique identifier of the custom emoji
    :type custom_emoji_id: :class:`int`
    
    """

    ID: str = Field("reactionTypeCustomEmoji", alias="@type")
    custom_emoji_id: int

    @staticmethod
    def read(q: dict) -> ReactionTypeCustomEmoji:
        return ReactionTypeCustomEmoji.construct(**q)


class ReactionTypeEmoji(ReactionType):
    """
    A reaction with an emoji
    
    :param emoji: Text representation of the reaction
    :type emoji: :class:`str`
    
    """

    ID: str = Field("reactionTypeEmoji", alias="@type")
    emoji: str

    @staticmethod
    def read(q: dict) -> ReactionTypeEmoji:
        return ReactionTypeEmoji.construct(**q)

