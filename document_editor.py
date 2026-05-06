from abc import ABC, abstractmethod
from typing import List, Optional

# ---------- Elements ----------

class DocumentElement(ABC):
    
    @abstractmethod
    def render(self) -> str:
        pass

class TextElement(DocumentElement):

    def __init__(self, text: str) -> None:
        self.text = text
    
    def render(self) -> str:
        return self.text

class ImageElement(DocumentElement):

    def __init__(self, path: str) -> None:
        self.path = path

    def render(self) -> str:
        return f"[Image: {self.path}]"


# ---------- Document ----------

class Document:

    def __init__(self) -> None:
        self.elements: List[DocumentElement] = []
    
    def add_element(self, element: DocumentElement) -> None:
        self.elements.append(element)

    def remove_element(self, element: DocumentElement) -> None:
        self.elements.remove(element)

    def get_content(self) -> List[str]:
        return [element.render() for element in self.elements]


# ---------- Saver ----------

class DocumentSaver(ABC):

    @abstractmethod
    def save(self, document: Document, path: str) -> None:
        pass


class TextFileSaver(DocumentSaver):

    def save(self, document: Document, path: str) -> None:
        with open(path, "w") as f:
            for content in document.get_content():
                f.write(content + "\n")
                

# ---------- Editor ----------

class Editor:

    def __init__(self, document: Document, saver: DocumentSaver, path: str) -> None:
        self.document: Document = document
        self.saver: DocumentSaver = saver
        self.path: str = None

    def save(self) -> None:
        if not self.path:
            raise Exception("Path does not exist!!!")
        self.saver.save(self.document, self.path)
    
    def save_as(self, path: str) -> None:
        self.path = path
        self.saver.save(self.document, self.path)
