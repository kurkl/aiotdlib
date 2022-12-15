# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import ChatAvailableReactions
from ..base_object import BaseObject


class SetChatAvailableReactions(BaseObject):
    """
    Changes reactions, available in a chat. Available for basic groups, supergroups, and channels. Requires can_change_info administrator right
    
    :param chat_id: Identifier of the chat
    :type chat_id: :class:`int`
    
    :param available_reactions: Reactions available in the chat. All emoji reactions must be active
    :type available_reactions: :class:`ChatAvailableReactions`
    
    """

    ID: str = Field("setChatAvailableReactions", alias="@type")
    chat_id: int
    available_reactions: ChatAvailableReactions

    @staticmethod
    def read(q: dict) -> SetChatAvailableReactions:
        return SetChatAvailableReactions.construct(**q)
