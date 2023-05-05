class Reply:
    def __init__(self, number: int, answer: str, confidence: float = 0, explanation: str = None):
        self.number = number
        self.answer = answer
        self.confidence = confidence
        self.explanation = explanation

    def __repr__(self):
        return f"Reply(number={self.number}, confidence={self.confidence}, answer={self.answer}) | {self.explanation}"
