# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .bot_info import BotInfo
from .chat_photo import ChatPhoto
from .formatted_text import FormattedText
from .premium_payment_option import PremiumPaymentOption
from ..base_object import BaseObject


class UserFullInfo(BaseObject):
    """
    Contains full information about a user
    
    :param photo: User profile photo; may be null if empty or unknown. If non-null, then it is the same photo as in user.profile_photo and chat.photo, defaults to None
    :type photo: :class:`ChatPhoto`, optional
    
    :param is_blocked: True, if the user is blocked by the current user
    :type is_blocked: :class:`bool`
    
    :param can_be_called: True, if the user can be called
    :type can_be_called: :class:`bool`
    
    :param supports_video_calls: True, if a video call can be created with the user
    :type supports_video_calls: :class:`bool`
    
    :param has_private_calls: True, if the user can't be called due to their privacy settings
    :type has_private_calls: :class:`bool`
    
    :param has_private_forwards: True, if the user can't be linked in forwarded messages due to their privacy settings
    :type has_private_forwards: :class:`bool`
    
    :param has_restricted_voice_and_video_note_messages: True, if voice and video notes can't be sent or forwarded to the user
    :type has_restricted_voice_and_video_note_messages: :class:`bool`
    
    :param need_phone_number_privacy_exception: True, if the current user needs to explicitly allow to share their phone number with the user when the method addContact is used
    :type need_phone_number_privacy_exception: :class:`bool`
    
    :param bio: A short user bio; may be null for bots, defaults to None
    :type bio: :class:`FormattedText`, optional
    
    :param premium_gift_options: The list of available options for gifting Telegram Premium to the user
    :type premium_gift_options: :class:`list[PremiumPaymentOption]`
    
    :param group_in_common_count: Number of group chats where both the other user and the current user are a member; 0 for the current user
    :type group_in_common_count: :class:`int`
    
    :param bot_info: For bots, information about the bot; may be null, defaults to None
    :type bot_info: :class:`BotInfo`, optional
    
    """

    ID: str = Field("userFullInfo", alias="@type")
    photo: typing.Optional[ChatPhoto] = None
    is_blocked: bool
    can_be_called: bool
    supports_video_calls: bool
    has_private_calls: bool
    has_private_forwards: bool
    has_restricted_voice_and_video_note_messages: bool
    need_phone_number_privacy_exception: bool
    bio: typing.Optional[FormattedText] = None
    premium_gift_options: list[PremiumPaymentOption]
    group_in_common_count: int
    bot_info: typing.Optional[BotInfo] = None

    @staticmethod
    def read(q: dict) -> UserFullInfo:
        return UserFullInfo.construct(**q)
