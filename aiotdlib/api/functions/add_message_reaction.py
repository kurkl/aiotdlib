# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import ReactionType
from ..base_object import BaseObject


class AddMessageReaction(BaseObject):
    """
    Adds a reaction to a message. Use getMessageAvailableReactions to receive the list of available reactions for the message
    
    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param reaction_type: Type of the reaction to add
    :type reaction_type: :class:`ReactionType`
    
    :param is_big: Pass true if the reaction is added with a big animation
    :type is_big: :class:`bool`
    
    :param update_recent_reactions: Pass true if the reaction needs to be added to recent reactions
    :type update_recent_reactions: :class:`bool`
    
    """

    ID: str = Field("addMessageReaction", alias="@type")
    chat_id: int
    message_id: int
    reaction_type: ReactionType
    is_big: bool
    update_recent_reactions: bool

    @staticmethod
    def read(q: dict) -> AddMessageReaction:
        return AddMessageReaction.construct(**q)
