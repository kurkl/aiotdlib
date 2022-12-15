# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import MessageTtl
from ..base_object import BaseObject


class SetDefaultMessageTtl(BaseObject):
    """
    Changes the default message Time To Live setting (self-destruct timer) for new chats
    
    :param ttl: New message TTL; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
    :type ttl: :class:`MessageTtl`
    
    """

    ID: str = Field("setDefaultMessageTtl", alias="@type")
    ttl: MessageTtl

    @staticmethod
    def read(q: dict) -> SetDefaultMessageTtl:
        return SetDefaultMessageTtl.construct(**q)
