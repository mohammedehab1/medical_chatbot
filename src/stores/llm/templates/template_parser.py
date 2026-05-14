import os
import importlib

class TemplateParser:
    def __init__(self, language: str = None, default_language: str = "ar"):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.default_language = default_language
        self.language = None

        self.set_language(language)

    def set_language(self, language: str | None):
        if not language:
            self.language = self.default_language
            return

        language_path = os.path.join(self.current_path, "locales", language)

        if os.path.exists(language_path):
            self.language = language
        else:
            self.language = self.default_language

    def detect_language(self, text: str):
        if not text:
            return self.default_language

        arabic_chars = sum(1 for c in text if '\u0600' <= c <= '\u06FF')

        if arabic_chars > len(text) * 0.3:
            return "ar"

        return "en"

    def get(self, group: str, key: str, vars: dict | None = None):
        vars = vars or {}

        if not group or not key:
            return None

        module_path = f"stores.llm.templates.locales.{self.language}.{group}"

        try:
            module = importlib.import_module(module_path)
        except ModuleNotFoundError:
            module_path = f"stores.llm.templates.locales.{self.default_language}.{group}"
            try:
                module = importlib.import_module(module_path)
            except ModuleNotFoundError:
                return None

        if not hasattr(module, key):
            return None

        template = getattr(module, key)
        return template.substitute(vars)