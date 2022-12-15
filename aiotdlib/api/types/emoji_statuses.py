# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .emoji_status import EmojiStatus
from ..base_object import BaseObject


class EmojiStatuses(BaseObject):
    """
    Contains a list of emoji statuses
    
    :param emoji_statuses: The list of emoji statuses
    :type emoji_statuses: :class:`list[EmojiStatus]`
    
    """

    ID: str = Field("emojiStatuses", alias="@type")
    emoji_statuses: list[EmojiStatus]

    @staticmethod
    def read(q: dict) -> EmojiStatuses:
        return EmojiStatuses.construct(**q)
