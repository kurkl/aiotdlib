# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message_sender import MessageSender
from .reaction_type import ReactionType
from ..base_object import BaseObject


class AddedReaction(BaseObject):
    """
    Represents a reaction applied to a message
    
    :param type_: Type of the reaction
    :type type_: :class:`ReactionType`
    
    :param sender_id: Identifier of the chat member, applied the reaction
    :type sender_id: :class:`MessageSender`
    
    """

    ID: str = Field("addedReaction", alias="@type")
    type_: ReactionType = Field(..., alias='type')
    sender_id: MessageSender

    @staticmethod
    def read(q: dict) -> AddedReaction:
        return AddedReaction.construct(**q)
