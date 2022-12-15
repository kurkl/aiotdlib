# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ReorderSupergroupActiveUsernames(BaseObject):
    """
    Changes order of active usernames of a supergroup or channel, requires owner privileges in the supergroup or channel
    
    :param supergroup_id: Identifier of the supergroup or channel
    :type supergroup_id: :class:`int`
    
    :param usernames: The new order of active usernames. All currently active usernames must be specified
    :type usernames: :class:`list[str]`
    
    """

    ID: str = Field("reorderSupergroupActiveUsernames", alias="@type")
    supergroup_id: int
    usernames: list[str]

    @staticmethod
    def read(q: dict) -> ReorderSupergroupActiveUsernames:
        return ReorderSupergroupActiveUsernames.construct(**q)
