class GptModel:
    def __init__(self, name: str, tokens: int):
        self.name = name
        self.tokens = tokens

    def __repr__(self):
        return f"GPTModel(name={self.name}, tokens={self.tokens})"
