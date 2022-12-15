# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import EmailAddressAuthentication
from ..base_object import BaseObject


class CheckAuthenticationEmailCode(BaseObject):
    """
    Checks the authentication of a email address. Works only when the current authorization state is authorizationStateWaitEmailCode
    
    :param code: Email address authentication to check
    :type code: :class:`EmailAddressAuthentication`
    
    """

    ID: str = Field("checkAuthenticationEmailCode", alias="@type")
    code: EmailAddressAuthentication

    @staticmethod
    def read(q: dict) -> CheckAuthenticationEmailCode:
        return CheckAuthenticationEmailCode.construct(**q)
