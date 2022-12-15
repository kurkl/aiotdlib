# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteForumTopic(BaseObject):
    """
    Deletes all messages in a forum topic; requires can_delete_messages administrator rights in the supergroup unless the user is creator of the topic, the topic has no messages from other users and has at most 11 messages
    
    :param chat_id: Identifier of the chat
    :type chat_id: :class:`int`
    
    :param message_thread_id: Message thread identifier of the forum topic
    :type message_thread_id: :class:`int`
    
    """

    ID: str = Field("deleteForumTopic", alias="@type")
    chat_id: int
    message_thread_id: int

    @staticmethod
    def read(q: dict) -> DeleteForumTopic:
        return DeleteForumTopic.construct(**q)
