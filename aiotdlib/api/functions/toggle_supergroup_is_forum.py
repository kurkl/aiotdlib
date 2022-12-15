# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleSupergroupIsForum(BaseObject):
    """
    Toggles whether the supergroup is a forum; requires owner privileges in the supergroup
    
    :param supergroup_id: Identifier of the supergroup
    :type supergroup_id: :class:`int`
    
    :param is_forum: New value of is_forum. A supergroup can be converted to a forum, only if it has at least getOption("forum_member_count_min") members
    :type is_forum: :class:`bool`
    
    """

    ID: str = Field("toggleSupergroupIsForum", alias="@type")
    supergroup_id: int
    is_forum: bool

    @staticmethod
    def read(q: dict) -> ToggleSupergroupIsForum:
        return ToggleSupergroupIsForum.construct(**q)
