import spacy


class TextPrep:
    def __init__(self, text: str) -> None:
        self.text = text
        self.nlp = spacy.load("en_core_web_sm")
        self.doc = None
        self.final_tokens = []

    def get_doc(self):
        doc = self.nlp(self.text)
        return doc

    def lowercasing(self):
        self.text = self.text.lower()

    def get_lemmas(self):
        self.doc = self.get_doc()
        for token in self.doc:
            if not token.is_punct and not token.is_stop:
                self.final_tokens.append(token.lemma_)
