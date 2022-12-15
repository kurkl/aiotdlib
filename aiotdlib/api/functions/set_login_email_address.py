# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetLoginEmailAddress(BaseObject):
    """
    Changes the login email address of the user. The change will not be applied until the new login email address is confirmed with `checkLoginEmailAddressCode`. To use Apple ID/Google ID instead of a email address, call `checkLoginEmailAddressCode` directly
    
    :param new_login_email_address: New login email address
    :type new_login_email_address: :class:`str`
    
    """

    ID: str = Field("setLoginEmailAddress", alias="@type")
    new_login_email_address: str

    @staticmethod
    def read(q: dict) -> SetLoginEmailAddress:
        return SetLoginEmailAddress.construct(**q)
