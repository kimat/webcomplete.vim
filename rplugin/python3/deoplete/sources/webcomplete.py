from .base import Base
from pathlib import Path

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

    def read(file):
        Path(file).read_text()

    def gather_candidates(self, context):
        context['is_async'] = False

        url = self.__url_file.read_text()

        if self.__url != url:
          self.__url = url
          self.__words = self.__words_file.read_text().splitlines()

        return [{'word': word} for word in self.__words]
