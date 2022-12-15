# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .forum_topic import ForumTopic
from ..base_object import BaseObject


class ForumTopics(BaseObject):
    """
    Describes a list of forum topics
    
    :param total_count: Approximate total number of forum topics found
    :type total_count: :class:`int`
    
    :param topics: List of forum topics
    :type topics: :class:`list[ForumTopic]`
    
    :param next_offset_date: Offset date for the next getForumTopics request
    :type next_offset_date: :class:`int`
    
    :param next_offset_message_id: Offset message identifier for the next getForumTopics request
    :type next_offset_message_id: :class:`int`
    
    :param next_offset_message_thread_id: Offset message thread identifier for the next getForumTopics request
    :type next_offset_message_thread_id: :class:`int`
    
    """

    ID: str = Field("forumTopics", alias="@type")
    total_count: int
    topics: list[ForumTopic]
    next_offset_date: int
    next_offset_message_id: int
    next_offset_message_thread_id: int

    @staticmethod
    def read(q: dict) -> ForumTopics:
        return ForumTopics.construct(**q)
