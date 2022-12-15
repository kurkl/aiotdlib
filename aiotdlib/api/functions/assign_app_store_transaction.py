# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import StorePaymentPurpose
from ..base_object import BaseObject


class AssignAppStoreTransaction(BaseObject):
    """
    Informs server about a purchase through App Store. For official applications only
    
    :param receipt: App Store receipt
    :type receipt: :class:`str`
    
    :param purpose: Transaction purpose
    :type purpose: :class:`StorePaymentPurpose`
    
    """

    ID: str = Field("assignAppStoreTransaction", alias="@type")
    receipt: str
    purpose: StorePaymentPurpose

    @staticmethod
    def read(q: dict) -> AssignAppStoreTransaction:
        return AssignAppStoreTransaction.construct(**q)
