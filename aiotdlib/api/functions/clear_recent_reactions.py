# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ClearRecentReactions(BaseObject):
    """
    Clears the list of recently used reactions
    
    """

    ID: str = Field("clearRecentReactions", alias="@type")

    @staticmethod
    def read(q: dict) -> ClearRecentReactions:
        return ClearRecentReactions.construct(**q)
