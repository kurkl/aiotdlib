# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class StorePaymentPurpose(BaseObject):
    """
    Describes a purpose of an in-store payment
    
    """

    ID: str = Field("storePaymentPurpose", alias="@type")

    
class StorePaymentPurposeGiftedPremium(StorePaymentPurpose):
    """
    The user gifted Telegram Premium to another user
    
    :param user_id: Identifier of the user for which Premium was gifted
    :type user_id: :class:`int`
    
    :param currency: ISO 4217 currency code of the payment currency
    :type currency: :class:`str`
    
    :param amount: Paid amount, in the smallest units of the currency
    :type amount: :class:`int`
    
    """

    ID: str = Field("storePaymentPurposeGiftedPremium", alias="@type")
    user_id: int
    currency: str
    amount: int

    @staticmethod
    def read(q: dict) -> StorePaymentPurposeGiftedPremium:
        return StorePaymentPurposeGiftedPremium.construct(**q)


class StorePaymentPurposePremiumSubscription(StorePaymentPurpose):
    """
    The user subscribed to Telegram Premium
    
    :param is_restore: Pass true if this is a restore of a Telegram Premium purchase; only for App Store
    :type is_restore: :class:`bool`
    
    """

    ID: str = Field("storePaymentPurposePremiumSubscription", alias="@type")
    is_restore: bool

    @staticmethod
    def read(q: dict) -> StorePaymentPurposePremiumSubscription:
        return StorePaymentPurposePremiumSubscription.construct(**q)

