# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class EditForumTopic(BaseObject):
    """
    Edits title and icon of a topic in a forum supergroup chat; requires can_manage_topics administrator rights in the supergroup unless the user is creator of the topic
    
    :param chat_id: Identifier of the chat
    :type chat_id: :class:`int`
    
    :param message_thread_id: Message thread identifier of the forum topic
    :type message_thread_id: :class:`int`
    
    :param name: New name of the topic; 0-128 characters. If empty, the previous topic name is kept, defaults to None
    :type name: :class:`str`, optional
    
    :param edit_icon_custom_emoji: Pass true to edit the icon of the topic. Icon of the General topic can't be edited
    :type edit_icon_custom_emoji: :class:`bool`
    
    :param icon_custom_emoji_id: Identifier of the new custom emoji for topic icon; pass 0 to remove the custom emoji. Ignored if edit_icon_custom_emoji is false. Telegram Premium users can use any custom emoji, other users can use only a custom emoji returned by getForumTopicDefaultIcons
    :type icon_custom_emoji_id: :class:`int`
    
    """

    ID: str = Field("editForumTopic", alias="@type")
    chat_id: int
    message_thread_id: int
    name: typing.Optional[str] = Field(None, max_length=128)
    edit_icon_custom_emoji: bool
    icon_custom_emoji_id: int

    @staticmethod
    def read(q: dict) -> EditForumTopic:
        return EditForumTopic.construct(**q)
