# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleSupergroupIsAggressiveAntiSpamEnabled(BaseObject):
    """
    Toggles whether aggressive anti-spam checks are enabled in the supergroup; requires can_delete_messages administrator right. Can be called only if the supergroup has at least getOption("aggressive_anti_spam_supergroup_member_count_min") members
    
    :param supergroup_id: The identifier of the supergroup, which isn't a broadcast group
    :type supergroup_id: :class:`int`
    
    :param is_aggressive_anti_spam_enabled: The new value of is_aggressive_anti_spam_enabled
    :type is_aggressive_anti_spam_enabled: :class:`bool`
    
    """

    ID: str = Field("toggleSupergroupIsAggressiveAntiSpamEnabled", alias="@type")
    supergroup_id: int
    is_aggressive_anti_spam_enabled: bool

    @staticmethod
    def read(q: dict) -> ToggleSupergroupIsAggressiveAntiSpamEnabled:
        return ToggleSupergroupIsAggressiveAntiSpamEnabled.construct(**q)
