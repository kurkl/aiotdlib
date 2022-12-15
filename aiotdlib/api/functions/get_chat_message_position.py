# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import SearchMessagesFilter
from ..base_object import BaseObject


class GetChatMessagePosition(BaseObject):
    """
    Returns approximate 1-based position of a message among messages, which can be found by the specified filter in the chat. Cannot be used in secret chats
    
    :param chat_id: Identifier of the chat in which to find message position
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param filter_: Filter for message content; searchMessagesFilterEmpty, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, and searchMessagesFilterFailedToSend are unsupported in this function
    :type filter_: :class:`SearchMessagesFilter`
    
    :param message_thread_id: If not 0, only messages in the specified thread will be considered; supergroups only
    :type message_thread_id: :class:`int`
    
    """

    ID: str = Field("getChatMessagePosition", alias="@type")
    chat_id: int
    message_id: int
    filter_: SearchMessagesFilter = Field(..., alias='filter')
    message_thread_id: int

    @staticmethod
    def read(q: dict) -> GetChatMessagePosition:
        return GetChatMessagePosition.construct(**q)
