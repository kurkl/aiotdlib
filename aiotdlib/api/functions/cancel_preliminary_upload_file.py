# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CancelPreliminaryUploadFile(BaseObject):
    """
    Stops the preliminary uploading of a file. Supported only for files uploaded by using preliminaryUploadFile. For other files the behavior is undefined
    
    :param file_id: Identifier of the file to stop uploading
    :type file_id: :class:`int`
    
    """

    ID: str = Field("cancelPreliminaryUploadFile", alias="@type")
    file_id: int

    @staticmethod
    def read(q: dict) -> CancelPreliminaryUploadFile:
        return CancelPreliminaryUploadFile.construct(**q)
