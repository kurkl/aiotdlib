# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetForumTopic(BaseObject):
    """
    Returns information about a forum topic
    
    :param chat_id: Identifier of the chat
    :type chat_id: :class:`int`
    
    :param message_thread_id: Message thread identifier of the forum topic
    :type message_thread_id: :class:`int`
    
    """

    ID: str = Field("getForumTopic", alias="@type")
    chat_id: int
    message_thread_id: int

    @staticmethod
    def read(q: dict) -> GetForumTopic:
        return GetForumTopic.construct(**q)
