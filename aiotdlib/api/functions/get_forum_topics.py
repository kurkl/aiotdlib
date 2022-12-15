# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetForumTopics(BaseObject):
    """
    Returns found forum topics in a forum chat. This is a temporary method for getting information about topic list from the server
    
    :param chat_id: Identifier of the forum chat
    :type chat_id: :class:`int`
    
    :param query: Query to search for in the forum topic's name
    :type query: :class:`str`
    
    :param offset_date: The date starting from which the results need to be fetched. Use 0 or any date in the future to get results from the last topic
    :type offset_date: :class:`int`
    
    :param offset_message_id: The message identifier of the last message in the last found topic, or 0 for the first request
    :type offset_message_id: :class:`int`
    
    :param offset_message_thread_id: The message thread identifier of the last found topic, or 0 for the first request
    :type offset_message_thread_id: :class:`int`
    
    :param limit: The maximum number of forum topics to be returned; up to 100. For optimal performance, the number of returned forum topics is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`int`
    
    """

    ID: str = Field("getForumTopics", alias="@type")
    chat_id: int
    query: str
    offset_date: int
    offset_message_id: int
    offset_message_thread_id: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetForumTopics:
        return GetForumTopics.construct(**q)
