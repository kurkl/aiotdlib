# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class EmojiStatus(BaseObject):
    """
    Describes a custom emoji to be shown instead of the Telegram Premium badge
    
    :param custom_emoji_id: Identifier of the custom emoji in stickerFormatTgs format. If the custom emoji belongs to the sticker set getOption("themed_emoji_statuses_sticker_set_id"), then it's color must be changed to the color of the Telegram Premium badge
    :type custom_emoji_id: :class:`int`
    
    """

    ID: str = Field("emojiStatus", alias="@type")
    custom_emoji_id: int

    @staticmethod
    def read(q: dict) -> EmojiStatus:
        return EmojiStatus.construct(**q)
