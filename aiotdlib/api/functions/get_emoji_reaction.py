# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetEmojiReaction(BaseObject):
    """
    Returns information about a emoji reaction. Returns a 404 error if the reaction is not found
    
    :param emoji: Text representation of the reaction
    :type emoji: :class:`str`
    
    """

    ID: str = Field("getEmojiReaction", alias="@type")
    emoji: str

    @staticmethod
    def read(q: dict) -> GetEmojiReaction:
        return GetEmojiReaction.construct(**q)
