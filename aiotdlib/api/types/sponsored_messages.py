# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .sponsored_message import SponsoredMessage
from ..base_object import BaseObject


class SponsoredMessages(BaseObject):
    """
    Contains a list of sponsored messages
    
    :param messages: List of sponsored messages
    :type messages: :class:`list[SponsoredMessage]`
    
    :param messages_between: The minimum number of messages between shown sponsored messages, or 0 if only one sponsored message must be shown after all ordinary messages
    :type messages_between: :class:`int`
    
    """

    ID: str = Field("sponsoredMessages", alias="@type")
    messages: list[SponsoredMessage]
    messages_between: int

    @staticmethod
    def read(q: dict) -> SponsoredMessages:
        return SponsoredMessages.construct(**q)
