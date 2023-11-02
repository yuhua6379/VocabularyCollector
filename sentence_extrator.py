import abc

from PyPDF2 import PdfReader

from word_extractor import WordExtractor


class SentenceExtractor(abc.ABC):
    @abc.abstractmethod
    def run(self) -> dict[str, int]:
        pass


class PdfSentenceExtractor(SentenceExtractor):
    def __init__(self, path: str):
        self.path = path
        self.we = WordExtractor()

    def run(self) -> dict[str, int]:
        with open('resources./friends_scripts_10_seasons.pdf', 'rb') as f:
            reader = PdfReader(f)
            num_pages = len(reader.pages)  # Get the number of pages

            # Read each page (page numbers start from 0)
            for page in range(num_pages):
                page_obj = reader.pages[page]  # Get a Page object
                text = page_obj.extract_text()  # Extract text from the page
                self.we(text)

        return self.we.get_word_collection()


def get_extractor(path: str) -> SentenceExtractor:
    return PdfSentenceExtractor(path)
