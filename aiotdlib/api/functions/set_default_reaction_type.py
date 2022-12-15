# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..types import ReactionType
from ..base_object import BaseObject


class SetDefaultReactionType(BaseObject):
    """
    Changes type of default reaction for the current user
    
    :param reaction_type: New type of the default reaction
    :type reaction_type: :class:`ReactionType`
    
    """

    ID: str = Field("setDefaultReactionType", alias="@type")
    reaction_type: ReactionType

    @staticmethod
    def read(q: dict) -> SetDefaultReactionType:
        return SetDefaultReactionType.construct(**q)
