from pydantic import BaseModel

class CreateDocumentModule(BaseModel):
    title: str
    body: str

class Document:
    def __init__(self, id: int, title: str, body: str) -> None:
        self.id = id
        self.title = title
        self.body = body 