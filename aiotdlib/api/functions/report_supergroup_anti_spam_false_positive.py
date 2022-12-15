# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ReportSupergroupAntiSpamFalsePositive(BaseObject):
    """
    Reports a false deletion of a message by aggressive anti-spam checks; requires administrator rights in the supergroup. Can be called only for messages from chatEventMessageDeleted with can_report_anti_spam_false_positive == true
    
    :param supergroup_id: Supergroup identifier
    :type supergroup_id: :class:`int`
    
    :param message_id: Identifier of the erroneously deleted message
    :type message_id: :class:`int`
    
    """

    ID: str = Field("reportSupergroupAntiSpamFalsePositive", alias="@type")
    supergroup_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> ReportSupergroupAntiSpamFalsePositive:
        return ReportSupergroupAntiSpamFalsePositive.construct(**q)
