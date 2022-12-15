# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ReadAllMessageThreadMentions(BaseObject):
    """
    Marks all mentions in a forum topic as read
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_thread_id: Message thread identifier in which mentions are marked as read
    :type message_thread_id: :class:`int`
    
    """

    ID: str = Field("readAllMessageThreadMentions", alias="@type")
    chat_id: int
    message_thread_id: int

    @staticmethod
    def read(q: dict) -> ReadAllMessageThreadMentions:
        return ReadAllMessageThreadMentions.construct(**q)
