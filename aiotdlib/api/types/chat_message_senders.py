# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_message_sender import ChatMessageSender
from ..base_object import BaseObject


class ChatMessageSenders(BaseObject):
    """
    Represents a list of message senders, which can be used to send messages in a chat
    
    :param senders: List of available message senders
    :type senders: :class:`list[ChatMessageSender]`
    
    """

    ID: str = Field("chatMessageSenders", alias="@type")
    senders: list[ChatMessageSender]

    @staticmethod
    def read(q: dict) -> ChatMessageSenders:
        return ChatMessageSenders.construct(**q)
