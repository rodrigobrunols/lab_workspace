"""

A class should have one reason to change. If a class mixes multiple concerns, split them.
This is the foundation of good class design.

"""


class Report:
    def generate_content(self) -> str:
        return "content"


class PDFPrinter:
    def print(self, report: Report) -> None:
        # PDF formatting
        pass


class FileStorage:
    def save(self, content: str) -> None:
        # file I/O
        pass
