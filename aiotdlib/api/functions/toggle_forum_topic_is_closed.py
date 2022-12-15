# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleForumTopicIsClosed(BaseObject):
    """
    Toggles whether a topic is closed in a forum supergroup chat; requires can_manage_topics administrator rights in the supergroup unless the user is creator of the topic
    
    :param chat_id: Identifier of the chat
    :type chat_id: :class:`int`
    
    :param message_thread_id: Message thread identifier of the forum topic
    :type message_thread_id: :class:`int`
    
    :param is_closed: Pass true to close the topic; pass false to reopen it
    :type is_closed: :class:`bool`
    
    """

    ID: str = Field("toggleForumTopicIsClosed", alias="@type")
    chat_id: int
    message_thread_id: int
    is_closed: bool

    @staticmethod
    def read(q: dict) -> ToggleForumTopicIsClosed:
        return ToggleForumTopicIsClosed.construct(**q)
