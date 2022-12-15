# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_notification_settings import ChatNotificationSettings
from .draft_message import DraftMessage
from .forum_topic_info import ForumTopicInfo
from .message import Message
from ..base_object import BaseObject


class ForumTopic(BaseObject):
    """
    Describes a forum topic
    
    :param info: Basic information about the topic
    :type info: :class:`ForumTopicInfo`
    
    :param last_message: Last message in the topic; may be null if unknown, defaults to None
    :type last_message: :class:`Message`, optional
    
    :param is_pinned: True, if the topic is pinned in the topic list
    :type is_pinned: :class:`bool`
    
    :param unread_count: Number of unread messages in the topic
    :type unread_count: :class:`int`
    
    :param last_read_inbox_message_id: Identifier of the last read incoming message
    :type last_read_inbox_message_id: :class:`int`
    
    :param last_read_outbox_message_id: Identifier of the last read outgoing message
    :type last_read_outbox_message_id: :class:`int`
    
    :param unread_mention_count: Number of unread messages with a mention/reply in the topic
    :type unread_mention_count: :class:`int`
    
    :param unread_reaction_count: Number of messages with unread reactions in the topic
    :type unread_reaction_count: :class:`int`
    
    :param notification_settings: Notification settings for the topic
    :type notification_settings: :class:`ChatNotificationSettings`
    
    :param draft_message: A draft of a message in the topic; may be null, defaults to None
    :type draft_message: :class:`DraftMessage`, optional
    
    """

    ID: str = Field("forumTopic", alias="@type")
    info: ForumTopicInfo
    last_message: typing.Optional[Message] = None
    is_pinned: bool
    unread_count: int
    last_read_inbox_message_id: int
    last_read_outbox_message_id: int
    unread_mention_count: int
    unread_reaction_count: int
    notification_settings: ChatNotificationSettings
    draft_message: typing.Optional[DraftMessage] = None

    @staticmethod
    def read(q: dict) -> ForumTopic:
        return ForumTopic.construct(**q)
