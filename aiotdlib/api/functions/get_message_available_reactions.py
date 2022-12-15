# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMessageAvailableReactions(BaseObject):
    """
    Returns reactions, which can be added to a message. The list can change after updateActiveEmojiReactions, updateChatAvailableReactions for the chat, or updateMessageInteractionInfo for the message
    
    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param row_size: Number of reaction per row, 5-25
    :type row_size: :class:`int`
    
    """

    ID: str = Field("getMessageAvailableReactions", alias="@type")
    chat_id: int
    message_id: int
    row_size: int

    @staticmethod
    def read(q: dict) -> GetMessageAvailableReactions:
        return GetMessageAvailableReactions.construct(**q)
