# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class UnpinAllMessageThreadMessages(BaseObject):
    """
    Removes all pinned messages from a forum topic; requires can_pin_messages rights in the supergroup
    
    :param chat_id: Identifier of the chat
    :type chat_id: :class:`int`
    
    :param message_thread_id: Message thread identifier in which messages will be unpinned
    :type message_thread_id: :class:`int`
    
    """

    ID: str = Field("unpinAllMessageThreadMessages", alias="@type")
    chat_id: int
    message_thread_id: int

    @staticmethod
    def read(q: dict) -> UnpinAllMessageThreadMessages:
        return UnpinAllMessageThreadMessages.construct(**q)
