# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import EmailAddressAuthentication
from ..base_object import BaseObject


class CheckLoginEmailAddressCode(BaseObject):
    """
    Checks the login email address authentication
    
    :param code: Email address authentication to check
    :type code: :class:`EmailAddressAuthentication`
    
    """

    ID: str = Field("checkLoginEmailAddressCode", alias="@type")
    code: EmailAddressAuthentication

    @staticmethod
    def read(q: dict) -> CheckLoginEmailAddressCode:
        return CheckLoginEmailAddressCode.construct(**q)
