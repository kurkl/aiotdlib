# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetAuthenticationEmailAddress(BaseObject):
    """
    Sets the email address of the user and sends an authentication code to the email address. Works only when the current authorization state is authorizationStateWaitEmailAddress
    
    :param email_address: The email address of the user
    :type email_address: :class:`str`
    
    """

    ID: str = Field("setAuthenticationEmailAddress", alias="@type")
    email_address: str

    @staticmethod
    def read(q: dict) -> SetAuthenticationEmailAddress:
        return SetAuthenticationEmailAddress.construct(**q)
