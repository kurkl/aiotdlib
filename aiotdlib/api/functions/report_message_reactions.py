# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import MessageSender
from ..base_object import BaseObject


class ReportMessageReactions(BaseObject):
    """
    Reports reactions set on a message to the Telegram moderators. Reactions on a message can be reported only if message.can_report_reactions
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param sender_id: Identifier of the sender, which added the reaction
    :type sender_id: :class:`MessageSender`
    
    """

    ID: str = Field("reportMessageReactions", alias="@type")
    chat_id: int
    message_id: int
    sender_id: MessageSender

    @staticmethod
    def read(q: dict) -> ReportMessageReactions:
        return ReportMessageReactions.construct(**q)
