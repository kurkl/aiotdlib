# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DisableAllSupergroupUsernames(BaseObject):
    """
    Disables all active non-editable usernames of a supergroup or channel, requires owner privileges in the supergroup or channel
    
    :param supergroup_id: Identifier of the supergroup or channel
    :type supergroup_id: :class:`int`
    
    """

    ID: str = Field("disableAllSupergroupUsernames", alias="@type")
    supergroup_id: int

    @staticmethod
    def read(q: dict) -> DisableAllSupergroupUsernames:
        return DisableAllSupergroupUsernames.construct(**q)
