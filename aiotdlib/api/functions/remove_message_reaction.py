# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import ReactionType
from ..base_object import BaseObject


class RemoveMessageReaction(BaseObject):
    """
    Removes a reaction from a message. A chosen reaction can always be removed
    
    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param reaction_type: Type of the reaction to remove
    :type reaction_type: :class:`ReactionType`
    
    """

    ID: str = Field("removeMessageReaction", alias="@type")
    chat_id: int
    message_id: int
    reaction_type: ReactionType

    @staticmethod
    def read(q: dict) -> RemoveMessageReaction:
        return RemoveMessageReaction.construct(**q)
