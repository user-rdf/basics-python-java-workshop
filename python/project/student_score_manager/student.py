from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Student:
    name: str
    scores: List[float] = field(default_factory=list)

    # ---------- score ops ----------
    def add_score(self, value: float) -> None:
        self._validate_score(value)
        # TODO: implement penambahan score

    def edit_score(self, index: int, new_value: float) -> None:
        if index < 0 or index >= len(self.scores):
            raise IndexError("Index nilai tidak valid")
        self._validate_score(new_value)
        # TODO: edit score dengan specific index

    def remove_score(self, index: int) -> None:
        if index < 0 or index >= len(self.scores):
            raise IndexError("Index nilai tidak valid")
        # TODO: hapus score dengan specific index

    # ---------- derived metrics ----------
    def average(self) -> float:
        # TODO: hitung rata-rata score, kembalikan 0.0 jika tidak ada score
        return sum(self.scores) / len(self.scores) if self.scores else 0.0

    def grade(self) -> str:
        avg = self.average()
        # TODO: kembalikan grade berdasarkan kondisi average
        return "E"

    # ---------- utils ----------
    # TODO: buat fungsi infoLine() yang return string dengan format:
    # Nama | scores=[..] | avg=.. | grade=..

    def to_dict(self) -> Dict:
        return {"name": self.name, "scores": self.scores}

    @staticmethod
    def from_dict(d: Dict) -> "Student":
        return Student(name=d["name"], scores=[float(x) for x in d.get("scores", [])])

    @staticmethod
    def _validate_score(value: float) -> None:
        try:
            v = float(value)
        except Exception as e:
            raise ValueError("Nilai harus berupa angka") from e
        if v < 0 or v > 100:
            raise ValueError("Score harus 0..100")
