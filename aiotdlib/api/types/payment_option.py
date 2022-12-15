# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PaymentOption(BaseObject):
    """
    Describes an additional payment option
    
    :param title: Title for the payment option
    :type title: :class:`str`
    
    :param url: Payment form URL to be opened in a web view
    :type url: :class:`str`
    
    """

    ID: str = Field("paymentOption", alias="@type")
    title: str
    url: str

    @staticmethod
    def read(q: dict) -> PaymentOption:
        return PaymentOption.construct(**q)
