from abc import ABC, abstractmethod
from typing import List, Optional

# ---------- Elements ----------

class DocumentElement:

    def __init__(self):
        self.styles = []

    def add_style(self, style):
        self.styles.append(style)

    def render(self):
        content = self._render_base()

        for style in self.styles:
            content = self.apply_style(style, content)

        return content

    def apply_style(self, style, content):
        raise NotImplementedError

    def _render_base(self):
        raise NotImplementedError


class TextElement(DocumentElement):

    def __init__(self, text):
        super().__init__()
        self.text = text

    def _render_base(self):
        return f"<txt>{self.text}</txt>"
    
    def apply_style(self, style, content):
        return style.apply_to_text(content)


class ImageElement(DocumentElement):

    def __init__(self, path):
        super().__init__()
        self.path = path

    def _render_base(self):
        return f"<img>{self.path}</img>"
    
    def apply_style(self, style, content):
        return style.apply_to_image(content)


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
        self.path: Optional[str] = None

    def save(self) -> None:
        if not self.path:
            raise Exception("Path does not exist!!!")
        self.saver.save(self.document, self.path)
    
    def save_as(self, path: str) -> None:
        self.path = path
        self.saver.save(self.document, self.path)


# ---------- Style ----------

class Style(ABC):

    def apply_to_text(self, content):
        return content

    def apply_to_image(self, content):
        return content


class Bold(Style):

    def apply_to_text(self, content):
        return f"<b>{content}</b>"
    
    def apply_to_image(self, content):
        return f"<imgb>{content}</imgb>"
    


# Document -> Elements -> Base Element + Styles (Design decision).
# Add new element -> make change to base style, and then add its styling to where ever you need.
# Add new style, apply where necessary a apply_to_* function and done.