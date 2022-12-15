# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .formatted_text import FormattedText
from .invoice import Invoice
from .order_info import OrderInfo
from .payment_option import PaymentOption
from .payment_provider import PaymentProvider
from .photo import Photo
from .saved_credentials import SavedCredentials
from ..base_object import BaseObject


class PaymentForm(BaseObject):
    """
    Contains information about an invoice payment form
    
    :param id: The payment form identifier
    :type id: :class:`int`
    
    :param invoice: Full information about the invoice
    :type invoice: :class:`Invoice`
    
    :param seller_bot_user_id: User identifier of the seller bot
    :type seller_bot_user_id: :class:`int`
    
    :param payment_provider_user_id: User identifier of the payment provider bot
    :type payment_provider_user_id: :class:`int`
    
    :param payment_provider: Information about the payment provider
    :type payment_provider: :class:`PaymentProvider`
    
    :param additional_payment_options: The list of additional payment options
    :type additional_payment_options: :class:`list[PaymentOption]`
    
    :param saved_order_info: Saved server-side order information; may be null, defaults to None
    :type saved_order_info: :class:`OrderInfo`, optional
    
    :param saved_credentials: The list of saved payment credentials
    :type saved_credentials: :class:`list[SavedCredentials]`
    
    :param can_save_credentials: True, if the user can choose to save credentials
    :type can_save_credentials: :class:`bool`
    
    :param need_password: True, if the user will be able to save credentials, if sets up a 2-step verification password
    :type need_password: :class:`bool`
    
    :param product_title: Product title
    :type product_title: :class:`str`
    
    :param product_description: Product description
    :type product_description: :class:`FormattedText`
    
    :param product_photo: Product photo; may be null, defaults to None
    :type product_photo: :class:`Photo`, optional
    
    """

    ID: str = Field("paymentForm", alias="@type")
    id: int
    invoice: Invoice
    seller_bot_user_id: int
    payment_provider_user_id: int
    payment_provider: PaymentProvider
    additional_payment_options: list[PaymentOption]
    saved_order_info: typing.Optional[OrderInfo] = None
    saved_credentials: list[SavedCredentials]
    can_save_credentials: bool
    need_password: bool
    product_title: str
    product_description: FormattedText
    product_photo: typing.Optional[Photo] = None

    @staticmethod
    def read(q: dict) -> PaymentForm:
        return PaymentForm.construct(**q)
