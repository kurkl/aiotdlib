# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetUserSupportInfo(BaseObject):
    """
    Returns support information for the given user; for Telegram support only
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    """

    ID: str = Field("getUserSupportInfo", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> GetUserSupportInfo:
        return GetUserSupportInfo.construct(**q)
