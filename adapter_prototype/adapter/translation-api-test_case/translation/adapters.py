from typing import List
from .services import *
from .model import *

class TranslationAdapter:
    def translate(self, request: TranslationRequest) -> str:
        pass

    def get_supported_languages(self) -> List[str]:
        pass


class MicrosoftTranslationAdapter(TranslationAdapter):
    def __init__(self):
        self.translate_api = MicrosoftTranslateApi()

    def translate(self, request: TranslationRequest) -> str:
        return self.translate_api.translate(request.text, request.source_language, request.target_language)

    def get_supported_languages(self) -> List[str]:
        return self.translate_api.get_supported_languages()


class GoogleTranslationAdapter(TranslationAdapter):
    def __init__(self):
        self.google_translate_api = GoogleTranslateApi()

    def translate(self, request: TranslationRequest) -> str:
        return self.google_translate_api.convert(self._to_google_translation_request(request))

    def _to_google_translation_request(self, request: TranslationRequest) -> GoogleTranslationRequest:
        return GoogleTranslationRequest(request.text, request.source_language, request.target_language, 0.8)

    def get_supported_languages(self) -> List[str]:
        return self.google_translate_api.get_languages()
