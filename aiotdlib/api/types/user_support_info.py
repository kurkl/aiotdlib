# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .formatted_text import FormattedText
from ..base_object import BaseObject


class UserSupportInfo(BaseObject):
    """
    Contains custom information about the user
    
    :param message: Information message
    :type message: :class:`FormattedText`
    
    :param author: Information author
    :type author: :class:`str`
    
    :param date: Information change date
    :type date: :class:`int`
    
    """

    ID: str = Field("userSupportInfo", alias="@type")
    message: FormattedText
    author: str
    date: int

    @staticmethod
    def read(q: dict) -> UserSupportInfo:
        return UserSupportInfo.construct(**q)
