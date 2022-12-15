# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .error import Error
from ..base_object import BaseObject


class SpeechRecognitionResult(BaseObject):
    """
    Describes result of speech recognition in a voice note
    
    """

    ID: str = Field("speechRecognitionResult", alias="@type")

    
class SpeechRecognitionResultError(SpeechRecognitionResult):
    """
    The speech recognition failed
    
    :param error: Received error
    :type error: :class:`Error`
    
    """

    ID: str = Field("speechRecognitionResultError", alias="@type")
    error: Error

    @staticmethod
    def read(q: dict) -> SpeechRecognitionResultError:
        return SpeechRecognitionResultError.construct(**q)


class SpeechRecognitionResultPending(SpeechRecognitionResult):
    """
    The speech recognition is ongoing
    
    :param partial_text: Partially recognized text
    :type partial_text: :class:`str`
    
    """

    ID: str = Field("speechRecognitionResultPending", alias="@type")
    partial_text: str

    @staticmethod
    def read(q: dict) -> SpeechRecognitionResultPending:
        return SpeechRecognitionResultPending.construct(**q)


class SpeechRecognitionResultText(SpeechRecognitionResult):
    """
    The speech recognition successfully finished
    
    :param text: Recognized text
    :type text: :class:`str`
    
    """

    ID: str = Field("speechRecognitionResultText", alias="@type")
    text: str

    @staticmethod
    def read(q: dict) -> SpeechRecognitionResultText:
        return SpeechRecognitionResultText.construct(**q)

