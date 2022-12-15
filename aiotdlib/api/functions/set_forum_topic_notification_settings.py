# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import ChatNotificationSettings
from ..base_object import BaseObject


class SetForumTopicNotificationSettings(BaseObject):
    """
    Changes the notification settings of a forum topic
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_thread_id: Message thread identifier of the forum topic
    :type message_thread_id: :class:`int`
    
    :param notification_settings: New notification settings for the forum topic. If the topic is muted for more than 366 days, it is considered to be muted forever
    :type notification_settings: :class:`ChatNotificationSettings`
    
    """

    ID: str = Field("setForumTopicNotificationSettings", alias="@type")
    chat_id: int
    message_thread_id: int
    notification_settings: ChatNotificationSettings

    @staticmethod
    def read(q: dict) -> SetForumTopicNotificationSettings:
        return SetForumTopicNotificationSettings.construct(**q)
