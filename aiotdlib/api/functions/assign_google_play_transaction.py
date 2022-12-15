# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import StorePaymentPurpose
from ..base_object import BaseObject


class AssignGooglePlayTransaction(BaseObject):
    """
    Informs server about a purchase through Google Play. For official applications only
    
    :param package_name: Application package name
    :type package_name: :class:`str`
    
    :param store_product_id: Identifier of the purchased store product
    :type store_product_id: :class:`str`
    
    :param purchase_token: Google Play purchase token
    :type purchase_token: :class:`str`
    
    :param purpose: Transaction purpose
    :type purpose: :class:`StorePaymentPurpose`
    
    """

    ID: str = Field("assignGooglePlayTransaction", alias="@type")
    package_name: str
    store_product_id: str
    purchase_token: str
    purpose: StorePaymentPurpose

    @staticmethod
    def read(q: dict) -> AssignGooglePlayTransaction:
        return AssignGooglePlayTransaction.construct(**q)
