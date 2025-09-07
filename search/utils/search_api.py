import re


class SearchAPI:
    def __init__(self, text):
        self.text = text.strip()
        self.paras = self._find_para_from_text()

    def _find_para_from_text(self):
        """Split text into paragraphs (separated by blank lines)."""
        paragraphs = [
            p.strip() for p in re.split(r"\n\s*\n", self.text) if p.strip()
        ]
        return paragraphs
