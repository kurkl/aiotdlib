# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message_sender import MessageSender
from ..base_object import BaseObject


class ChatMessageSender(BaseObject):
    """
    Represents a message sender, which can be used to send messages in a chat
    
    :param sender: Available message senders
    :type sender: :class:`MessageSender`
    
    :param needs_premium: True, if Telegram Premium is needed to use the message sender
    :type needs_premium: :class:`bool`
    
    """

    ID: str = Field("chatMessageSender", alias="@type")
    sender: MessageSender
    needs_premium: bool

    @staticmethod
    def read(q: dict) -> ChatMessageSender:
        return ChatMessageSender.construct(**q)
