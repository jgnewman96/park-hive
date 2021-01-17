import re
from abc import ABC, abstractmethod
from typing import List, Tuple

import frontmatter


class MarkdownFile:
    def __init__(self, filename: str):

        self.filetext = frontmatter.load(filename).content

        self.operations = [QuoteParser(), SideNoteParser()]

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
            insert_text = f"""<blockquote>
                               <p><i>{important_text}</i>
                               </blockquote>"""

            end_block = end + len(self.end_id) + 1
            start_block = start - 1
            replace_text = text[start_block:end_block]
            text = text.replace(replace_text, insert_text)

        return text


class SideNoteParser:
    def parse(self, text: str) -> str:
        pattern = re.compile("\[\^[0-9]]")
        matches = pattern.findall(text)
        start_idxs: List[int] = [m.start() for m in re.finditer(pattern, text)]
        num_footnotes = int(len(start_idxs) / 2)
        inline_idxs = start_idxs[0:num_footnotes]
        end_idxs: List[int] = start_idxs[num_footnotes:]

        # adding one more for the last note
        end_idxs.append(len(text))
        footnote_texts: List[str] = []

        for i in range(0, len(end_idxs) - 1):
            start_idx = end_idxs[i] + 6
            end_idx = end_idxs[i + 1]
            footnote_texts.append(text[start_idx:end_idx].strip("\n"))

        text = text[0 : end_idxs[0]]

        for i, footnote_str in enumerate(matches[0:num_footnotes]):
            replacement_text = f"<sup>{i+1}</sup> <span class='sidenote'> <sup>{i+1}</sup> {footnote_texts[i]}</span>"
            text = text.replace(footnote_str, replacement_text)

        return text
