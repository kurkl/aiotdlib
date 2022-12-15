# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetDefaultMessageTtl(BaseObject):
    """
    Returns default message Time To Live setting (self-destruct timer) for new chats
    
    """

    ID: str = Field("getDefaultMessageTtl", alias="@type")

    @staticmethod
    def read(q: dict) -> GetDefaultMessageTtl:
        return GetDefaultMessageTtl.construct(**q)
