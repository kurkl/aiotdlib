# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RemoteFile(BaseObject):
    """
    Represents a remote file
    
    Params:
        id (:class:`str`)
            Remote file identifier; may be empty. Can be used by the current user across application restarts or even from other devices. Uniquely identifies a file, but a file can have a lot of different valid identifiers. If the ID starts with "http://" or "https://", it represents the HTTP URL of the file. TDLib is currently unable to download files if only their URL is known. If downloadFile is called on such a file or if it is sent to a secret chat, TDLib starts a file generation process by sending updateFileGenerationStart to the application with the HTTP URL in the original_path and "#url#" as the conversion string. Application should generate the file by downloading it to the specified location
        
        unique_id (:class:`str`)
            Unique file identifier; may be empty if unknown. The unique file identifier which is the same for the same file even for different users and is persistent over time
        
        is_uploading_active (:class:`bool`)
            True, if the file is currently being uploaded (or a remote copy is being generated by some other means)
        
        is_uploading_completed (:class:`bool`)
            True, if a remote copy is fully available
        
        uploaded_size (:class:`int`)
            Size of the remote available part of the file, in bytes; 0 if unknown
        
    """

    ID: str = Field("remoteFile", alias="@type")
    id: str
    unique_id: str
    is_uploading_active: bool
    is_uploading_completed: bool
    uploaded_size: int

    @staticmethod
    def read(q: dict) -> RemoteFile:
        return RemoteFile.construct(**q)
