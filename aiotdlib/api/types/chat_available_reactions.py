# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .reaction_type import ReactionType
from ..base_object import BaseObject


class ChatAvailableReactions(BaseObject):
    """
    Describes reactions available in the chat
    
    """

    ID: str = Field("chatAvailableReactions", alias="@type")

    
class ChatAvailableReactionsAll(ChatAvailableReactions):
    """
    All reactions are available in the chat
    
    """

    ID: str = Field("chatAvailableReactionsAll", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatAvailableReactionsAll:
        return ChatAvailableReactionsAll.construct(**q)


class ChatAvailableReactionsSome(ChatAvailableReactions):
    """
    Only specific reactions are available in the chat
    
    :param reactions: The list of reactions
    :type reactions: :class:`list[ReactionType]`
    
    """

    ID: str = Field("chatAvailableReactionsSome", alias="@type")
    reactions: list[ReactionType]

    @staticmethod
    def read(q: dict) -> ChatAvailableReactionsSome:
        return ChatAvailableReactionsSome.construct(**q)

