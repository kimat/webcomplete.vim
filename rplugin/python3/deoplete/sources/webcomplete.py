from .base import Base
from pathlib import Path
from bs4 import BeautifulSoup
import re

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'webcomplete'
        self.kind = 'keyword'
        self.mark = '[web]'
        self.input_pattern = r'[\c]*'
        self.rank = 4

        self.__url = ""
        self.__url_file = Path("/dev/shm/ff_current_url")
        self.__words = []
        self.__words_file = Path("/dev/shm/ff_current_words")
        self.__source_file = Path("/dev/shm/ff_current_source")

    def gather_candidates(self, context):
        context['is_async'] = False

        url = self.__url_file.read_text()

        if self.__url != url:
            self.__url = url
            self.__source = self.__source_file.read_text()
            soup = BeautifulSoup(self.__source, "html")
            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()    # rip it out
            text = soup.get_text()
            words = re.compile('\S+').findall(text)
            print("here")
            self.__words = sorted(set(words))

        return [{'word': word} for word in self.__words]
