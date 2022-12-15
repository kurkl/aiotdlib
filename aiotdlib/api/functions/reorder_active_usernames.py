# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ReorderActiveUsernames(BaseObject):
    """
    Changes order of active usernames of the current user
    
    :param usernames: The new order of active usernames. All currently active usernames must be specified
    :type usernames: :class:`list[str]`
    
    """

    ID: str = Field("reorderActiveUsernames", alias="@type")
    usernames: list[str]

    @staticmethod
    def read(q: dict) -> ReorderActiveUsernames:
        return ReorderActiveUsernames.construct(**q)
