# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ResendLoginEmailAddressCode(BaseObject):
    """
    Resends the login email address verification code
    
    """

    ID: str = Field("resendLoginEmailAddressCode", alias="@type")

    @staticmethod
    def read(q: dict) -> ResendLoginEmailAddressCode:
        return ResendLoginEmailAddressCode.construct(**q)
