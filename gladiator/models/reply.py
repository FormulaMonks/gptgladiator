class Reply:
    def __init__(self, number: int, answer: str, confidence: float = 0):
        self.number = number
        self.answer = answer
        self.confidence = confidence

    def __repr__(self):
        return f"Reply(number={self.number}, confidence={self.confidence}, answer={self.answer})"
