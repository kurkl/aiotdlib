# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class MessageTtl(BaseObject):
    """
    Contains default message Time To Live setting (self-destruct timer) for new chats
    
    :param ttl: Message TTL setting, in seconds. If 0, then messages aren't deleted automatically
    :type ttl: :class:`int`
    
    """

    ID: str = Field("messageTtl", alias="@type")
    ttl: int

    @staticmethod
    def read(q: dict) -> MessageTtl:
        return MessageTtl.construct(**q)
