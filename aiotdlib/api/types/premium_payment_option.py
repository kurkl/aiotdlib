# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .internal_link_type import InternalLinkType
from ..base_object import BaseObject


class PremiumPaymentOption(BaseObject):
    """
    Describes an option for buying Telegram Premium to a user
    
    :param currency: ISO 4217 currency code for Telegram Premium subscription payment
    :type currency: :class:`str`
    
    :param amount: The amount to pay, in the smallest units of the currency
    :type amount: :class:`int`
    
    :param discount_percentage: The discount associated with this option, as a percentage
    :type discount_percentage: :class:`int`
    
    :param month_count: Number of month the Telegram Premium subscription will be active
    :type month_count: :class:`int`
    
    :param store_product_id: Identifier of the store product associated with the option
    :type store_product_id: :class:`str`
    
    :param payment_link: An internal link to be opened for buying Telegram Premium to the user if store payment isn't possible; may be null if direct payment isn't available, defaults to None
    :type payment_link: :class:`InternalLinkType`, optional
    
    """

    ID: str = Field("premiumPaymentOption", alias="@type")
    currency: str
    amount: int
    discount_percentage: int
    month_count: int
    store_product_id: str
    payment_link: typing.Optional[InternalLinkType] = None

    @staticmethod
    def read(q: dict) -> PremiumPaymentOption:
        return PremiumPaymentOption.construct(**q)
