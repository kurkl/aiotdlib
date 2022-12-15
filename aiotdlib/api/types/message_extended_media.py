# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .formatted_text import FormattedText
from .minithumbnail import Minithumbnail
from .photo import Photo
from .video import Video
from ..base_object import BaseObject


class MessageExtendedMedia(BaseObject):
    """
    Describes a media, which is attached to an invoice
    
    """

    ID: str = Field("messageExtendedMedia", alias="@type")

    
class MessageExtendedMediaPhoto(MessageExtendedMedia):
    """
    The media is a photo
    
    :param photo: The photo
    :type photo: :class:`Photo`
    
    :param caption: Photo caption
    :type caption: :class:`FormattedText`
    
    """

    ID: str = Field("messageExtendedMediaPhoto", alias="@type")
    photo: Photo
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> MessageExtendedMediaPhoto:
        return MessageExtendedMediaPhoto.construct(**q)


class MessageExtendedMediaPreview(MessageExtendedMedia):
    """
    The media is hidden until the invoice is paid
    
    :param width: Media width; 0 if unknown
    :type width: :class:`int`
    
    :param height: Media height; 0 if unknown
    :type height: :class:`int`
    
    :param duration: Media duration; 0 if unknown
    :type duration: :class:`int`
    
    :param minithumbnail: Media minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    
    :param caption: Media caption
    :type caption: :class:`FormattedText`
    
    """

    ID: str = Field("messageExtendedMediaPreview", alias="@type")
    width: int
    height: int
    duration: int
    minithumbnail: typing.Optional[Minithumbnail] = None
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> MessageExtendedMediaPreview:
        return MessageExtendedMediaPreview.construct(**q)


class MessageExtendedMediaUnsupported(MessageExtendedMedia):
    """
    The media is unuspported
    
    :param caption: Media caption
    :type caption: :class:`FormattedText`
    
    """

    ID: str = Field("messageExtendedMediaUnsupported", alias="@type")
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> MessageExtendedMediaUnsupported:
        return MessageExtendedMediaUnsupported.construct(**q)


class MessageExtendedMediaVideo(MessageExtendedMedia):
    """
    The media is a video
    
    :param video: The video
    :type video: :class:`Video`
    
    :param caption: Photo caption
    :type caption: :class:`FormattedText`
    
    """

    ID: str = Field("messageExtendedMediaVideo", alias="@type")
    video: Video
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> MessageExtendedMediaVideo:
        return MessageExtendedMediaVideo.construct(**q)

