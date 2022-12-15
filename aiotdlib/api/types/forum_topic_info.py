# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .forum_topic_icon import ForumTopicIcon
from .message_sender import MessageSender
from ..base_object import BaseObject


class ForumTopicInfo(BaseObject):
    """
    Contains basic information about a forum topic
    
    :param message_thread_id: Message thread identifier of the topic
    :type message_thread_id: :class:`int`
    
    :param name: Name of the topic
    :type name: :class:`str`
    
    :param icon: Icon of the topic
    :type icon: :class:`ForumTopicIcon`
    
    :param creation_date: Date the topic was created
    :type creation_date: :class:`int`
    
    :param creator_id: Identifier of the creator of the topic
    :type creator_id: :class:`MessageSender`
    
    :param is_general: True, if the topic is the General topic list
    :type is_general: :class:`bool`
    
    :param is_outgoing: True, if the topic was created by the current user
    :type is_outgoing: :class:`bool`
    
    :param is_closed: True, if the topic is closed
    :type is_closed: :class:`bool`
    
    :param is_hidden: True, if the topic is hidden above the topic list and closed; for General topic only
    :type is_hidden: :class:`bool`
    
    """

    ID: str = Field("forumTopicInfo", alias="@type")
    message_thread_id: int
    name: str
    icon: ForumTopicIcon
    creation_date: int
    creator_id: MessageSender
    is_general: bool
    is_outgoing: bool
    is_closed: bool
    is_hidden: bool

    @staticmethod
    def read(q: dict) -> ForumTopicInfo:
        return ForumTopicInfo.construct(**q)
