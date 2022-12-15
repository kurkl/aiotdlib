# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import FormattedText
from ..base_object import BaseObject


class SetUserSupportInfo(BaseObject):
    """
    Sets support information for the given user; for Telegram support only
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    :param message: New information message
    :type message: :class:`FormattedText`
    
    """

    ID: str = Field("setUserSupportInfo", alias="@type")
    user_id: int
    message: FormattedText

    @staticmethod
    def read(q: dict) -> SetUserSupportInfo:
        return SetUserSupportInfo.construct(**q)
