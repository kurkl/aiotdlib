# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .file import File
from .minithumbnail import Minithumbnail
from .speech_recognition_result import SpeechRecognitionResult
from .thumbnail import Thumbnail
from ..base_object import BaseObject


class VideoNote(BaseObject):
    """
    Describes a video note. The video must be equal in width and height, cropped to a circle, and stored in MPEG4 format
    
    :param duration: Duration of the video, in seconds; as defined by the sender
    :type duration: :class:`int`
    
    :param waveform: A waveform representation of the video note's audio in 5-bit format; may be empty if unknown
    :type waveform: :class:`str`
    
    :param length: Video width and height; as defined by the sender
    :type length: :class:`int`
    
    :param minithumbnail: Video minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    
    :param thumbnail: Video thumbnail in JPEG format; as defined by the sender; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    
    :param speech_recognition_result: Result of speech recognition in the video note; may be null, defaults to None
    :type speech_recognition_result: :class:`SpeechRecognitionResult`, optional
    
    :param video: File containing the video
    :type video: :class:`File`
    
    """

    ID: str = Field("videoNote", alias="@type")
    duration: int
    waveform: str
    length: int
    minithumbnail: typing.Optional[Minithumbnail] = None
    thumbnail: typing.Optional[Thumbnail] = None
    speech_recognition_result: typing.Optional[SpeechRecognitionResult] = None
    video: File

    @staticmethod
    def read(q: dict) -> VideoNote:
        return VideoNote.construct(**q)
