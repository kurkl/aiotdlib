# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .available_reaction import AvailableReaction
from ..base_object import BaseObject


class AvailableReactions(BaseObject):
    """
    Represents a list of reactions that can be added to a message
    
    :param top_reactions: List of reactions to be shown at the top
    :type top_reactions: :class:`list[AvailableReaction]`
    
    :param recent_reactions: List of recently used reactions
    :type recent_reactions: :class:`list[AvailableReaction]`
    
    :param popular_reactions: List of popular reactions
    :type popular_reactions: :class:`list[AvailableReaction]`
    
    :param allow_custom_emoji: True, if custom emoji reactions could be added by Telegram Premium subscribers
    :type allow_custom_emoji: :class:`bool`
    
    """

    ID: str = Field("availableReactions", alias="@type")
    top_reactions: list[AvailableReaction]
    recent_reactions: list[AvailableReaction]
    popular_reactions: list[AvailableReaction]
    allow_custom_emoji: bool

    @staticmethod
    def read(q: dict) -> AvailableReactions:
        return AvailableReactions.construct(**q)
