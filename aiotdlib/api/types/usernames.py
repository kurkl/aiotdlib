# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Usernames(BaseObject):
    """
    Describes usernames assigned to a user, a supergroup, or a channel
    
    :param active_usernames: List of active usernames; the first one must be shown as the primary username. The order of active usernames can be changed with reorderActiveUsernames or reorderSupergroupActiveUsernames
    :type active_usernames: :class:`list[str]`
    
    :param disabled_usernames: List of currently disabled usernames; the username can be activated with toggleUsernameIsActive/toggleSupergroupUsernameIsActive
    :type disabled_usernames: :class:`list[str]`
    
    :param editable_username: The active username, which can be changed with setUsername/setSupergroupUsername
    :type editable_username: :class:`str`
    
    """

    ID: str = Field("usernames", alias="@type")
    active_usernames: list[str]
    disabled_usernames: list[str]
    editable_username: str

    @staticmethod
    def read(q: dict) -> Usernames:
        return Usernames.construct(**q)
