class GptModel:
    def __init__(self, name: str, tokens: int):
        """
        Initialize a `GPTModel` with a given `name` and `tokens` limit.

        This is how you specify which model to use for generating drafts
        and/or grading them within `Gladiator`.

        For example:
        ```
        gladiator.generate_model = GptModel('gpt-3.5-turbo', 4000)
        ```
        """
        self.name = name
        self.tokens = tokens

    def __repr__(self):
        return f"GPTModel(name={self.name}, tokens={self.tokens})"
