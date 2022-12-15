# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .formatted_text import FormattedText
from .premium_feature_promotion_animation import PremiumFeaturePromotionAnimation
from .premium_payment_option import PremiumPaymentOption
from ..base_object import BaseObject


class PremiumState(BaseObject):
    """
    Contains state of Telegram Premium subscription and promotion videos for Premium features
    
    :param state: Text description of the state of the current Premium subscription; may be empty if the current user has no Telegram Premium subscription
    :type state: :class:`FormattedText`
    
    :param payment_options: The list of available options for buying Telegram Premium
    :type payment_options: :class:`list[PremiumPaymentOption]`
    
    :param animations: The list of available promotion animations for Premium features
    :type animations: :class:`list[PremiumFeaturePromotionAnimation]`
    
    """

    ID: str = Field("premiumState", alias="@type")
    state: FormattedText
    payment_options: list[PremiumPaymentOption]
    animations: list[PremiumFeaturePromotionAnimation]

    @staticmethod
    def read(q: dict) -> PremiumState:
        return PremiumState.construct(**q)
