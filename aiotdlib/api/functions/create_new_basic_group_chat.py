# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CreateNewBasicGroupChat(BaseObject):
    """
    Creates a new basic group and sends a corresponding messageBasicGroupChatCreate. Returns the newly created chat
    
    :param user_ids: Identifiers of users to be added to the basic group
    :type user_ids: :class:`list[int]`
    
    :param title: Title of the new basic group; 1-128 characters
    :type title: :class:`str`
    
    :param message_ttl: Message TTL value, in seconds; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
    :type message_ttl: :class:`int`
    
    """

    ID: str = Field("createNewBasicGroupChat", alias="@type")
    user_ids: list[int]
    title: str = Field(..., min_length=1, max_length=128)
    message_ttl: int

    @staticmethod
    def read(q: dict) -> CreateNewBasicGroupChat:
        return CreateNewBasicGroupChat.construct(**q)
