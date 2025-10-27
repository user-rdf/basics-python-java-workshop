from typing import List, Dict, Optional

class Student:
    def __init__(self, name: str, scores: Optional[List[float]] = None):
        self.name = name
        self.scores = scores or []

    def add_score(self, value: float) -> None:
        # TODO: add score dengan validasi 0..100
        pass

    def average(self) -> float:
        # TODO: kembalikan 0 jika belum ada nilai
        # hint: gunakan sum() dan len()
        return 0.0

    def grade(self) -> str:
        avg = self.average()
        # TODO: mapping grade berdasarkan average
        return "E"

    def to_dict(self) -> Dict:
        return {"name": self.name, "scores": self.scores}

    @staticmethod
    def from_dict(d: Dict) -> "Student":
        return Student(name=d["name"], scores=d.get("scores", []))
