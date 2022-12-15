# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import EmojiStatus
from ..base_object import BaseObject


class SetEmojiStatus(BaseObject):
    """
    Changes the emoji status of the current user; for Telegram Premium users only
    
    :param emoji_status: New emoji status; pass null to switch to the default badge
    :type emoji_status: :class:`EmojiStatus`
    
    :param duration: Duration of the status, in seconds; pass 0 to keep the status active until it will be changed manually
    :type duration: :class:`int`
    
    """

    ID: str = Field("setEmojiStatus", alias="@type")
    emoji_status: EmojiStatus
    duration: int

    @staticmethod
    def read(q: dict) -> SetEmojiStatus:
        return SetEmojiStatus.construct(**q)
