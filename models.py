from dataclasses import dataclass


@dataclass
class Fieldnames:
    title: str
    modification_date: str
    id: str
    text: str
    hyperlink: str

    @property
    def tolist(self):
        fieldnames = [
            self.title, 
            self.modification_date,
            self.id,
            self.text,
            self.hyperlink,
        ]
        return fieldnames


fieldnames = Fieldnames(
    title='short_description',
    modification_date='published',
    id='number',
    text='text',
    hyperlink='u_knowledge_permalink',
)
