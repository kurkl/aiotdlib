# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import StorePaymentPurpose
from ..base_object import BaseObject


class CanPurchasePremium(BaseObject):
    """
    Checks whether Telegram Premium purchase is possible. Must be called before in-store Premium purchase
    
    :param purpose: Transaction purpose
    :type purpose: :class:`StorePaymentPurpose`
    
    """

    ID: str = Field("canPurchasePremium", alias="@type")
    purpose: StorePaymentPurpose

    @staticmethod
    def read(q: dict) -> CanPurchasePremium:
        return CanPurchasePremium.construct(**q)
