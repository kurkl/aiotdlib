# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleGeneralForumTopicIsHidden(BaseObject):
    """
    Toggles whether a General topic is hidden in a forum supergroup chat; requires can_manage_topics administrator rights in the supergroup
    
    :param chat_id: Identifier of the chat
    :type chat_id: :class:`int`
    
    :param is_hidden: Pass true to hide and close the General topic; pass false to unhide it
    :type is_hidden: :class:`bool`
    
    """

    ID: str = Field("toggleGeneralForumTopicIsHidden", alias="@type")
    chat_id: int
    is_hidden: bool

    @staticmethod
    def read(q: dict) -> ToggleGeneralForumTopicIsHidden:
        return ToggleGeneralForumTopicIsHidden.construct(**q)
