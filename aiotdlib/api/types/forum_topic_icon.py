# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ForumTopicIcon(BaseObject):
    """
    Describes a forum topic icon
    
    :param color: Color of the topic icon in RGB format
    :type color: :class:`int`
    
    :param custom_emoji_id: Unique identifier of the custom emoji shown on the topic icon; 0 if none
    :type custom_emoji_id: :class:`int`
    
    """

    ID: str = Field("forumTopicIcon", alias="@type")
    color: int
    custom_emoji_id: int

    @staticmethod
    def read(q: dict) -> ForumTopicIcon:
        return ForumTopicIcon.construct(**q)
