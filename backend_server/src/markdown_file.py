import re
from abc import ABC, abstractmethod
from typing import List, Tuple


class MarkdownFile:
    def __init__(self, filename: str):
        f = open(filename, "r")

        self.filetext = f.read()

        self.operations = [QuoteParser()]

    def render(self) -> str:
        text: str = self.filetext
        for operation in self.operations:
            text = operation.parse(text)
        return text


class TextParser(ABC):
    identifier: str

    def __init__(self) -> None:
        self.start_id = f"{{< {self.identifier} >}}"
        self.end_id = f"{{< /{self.identifier} >}}"

    @abstractmethod
    def parse(self, text: str) -> str:
        raise NotImplementedError

    def _find(self, text: str) -> List[Tuple[int, int]]:
        start_idx = [m.start() for m in re.finditer(self.start_id, text)]
        end_idx = [m.start() for m in re.finditer(self.end_id, text)]
        return list(zip(start_idx, end_idx))


class QuoteParser(TextParser):
    identifier = "quote"

    def parse(self, text: str) -> str:
        instances = self._find(text)
        for start, end in reversed(instances):
            start_important = start + len(self.start_id) + 1
            end_important = end - 1
            important_text = text[start_important:end_important]
            insert_text = f"""<blockquote
                               style="background-color: lightgoldenrodyellow;  border-width: 1px; border-style: solid; border-left: 3px solid;">
                               <p><i>{important_text}</i>
                               </blockquote>"""

            end_block = end + len(self.end_id) + 1
            start_block = start - 1
            replace_text = text[start_block:end_block]
            text = text.replace(replace_text, insert_text)

        return text
