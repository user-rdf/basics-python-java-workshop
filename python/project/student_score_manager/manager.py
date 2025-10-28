from __future__ import annotations
from typing import List, Optional
from pathlib import Path
from student import Student
from storage import save_to_file, load_from_file, DEFAULT_PATH


class StudentManager:
    def __init__(self) -> None:
        self.students: List[Student] = []

    # ---------- menu ----------
    def menu(self) -> None:
        while True:
            print("\n=== Student Score Manager (Python) ===")
            print("1) Tambah mahasiswa")
            print("2) Lihat semua mahasiswa")
            print("3) Tambah nilai ke mahasiswa")
            print("4) Edit nilai mahasiswa")
            print("5) Hapus nilai mahasiswa")
            print("6) Edit nama mahasiswa")
            print("7) Hapus mahasiswa")
            print("8) Statistik kelas (rata-rata & top student)")
            print("9) Simpan data (JSON)")
            print("10) Muat data (JSON)")
            print("0) Keluar")
            choice = input("Pilih menu: ").strip()

            try:
                if choice == "1":
                    self.add_student()
                elif choice == "2":
                    self.list_students()
                elif choice == "3":
                    self.add_score_to_student()
                elif choice == "4":
                    self.edit_student_score()
                elif choice == "5":
                    self.delete_student_score()
                elif choice == "6":
                    self.edit_student_name()
                elif choice == "7":
                    self.delete_student()
                elif choice == "8":
                    self.class_stats()
                elif choice == "9":
                    self.save_json()
                elif choice == "10":
                    self.load_json()
                elif choice == "0":
                    print("Sampai jumpa 👋")
                    return
                else:
                    print("Menu tidak dikenal.")
            except Exception as e:
                print(f"❌ Error: {e}")

    # ---------- helpers ----------
    def _find_by_name(self, name: str) -> Optional[Student]:
        name_lower = name.lower()
        for s in self.students:
            if s.name.lower() == name_lower:
                return s
        return None

    @staticmethod
    def _parse_score(raw: str) -> float:
        try:
            val = float(raw)
        except Exception as e:
            raise ValueError("Masukkan angka yang valid") from e
        if val < 0 or val > 100:
            raise ValueError("Score harus 0..100")
        return val

    # ---------- actions ----------
    def add_student(self) -> None:
        name = input("Nama mahasiswa: ").strip()
        if not name:
            print("Nama tidak boleh kosong.")
            return
        if self._find_by_name(name):
            print("Mahasiswa sudah ada.")
            return

        s = Student(name)
        # TODO: implement penambahan mahasiswa
        # Hint: gunakan loop untuk input banyak score dari user, pakai method _parse_score() dan add_score(), lalu tambahkan ke students List
        print("✅ Mahasiswa ditambahkan.")

    def list_students(self) -> None:
        if not self.students:
            print("Belum ada data.")
            return
        print("\n== Daftar Mahasiswa ==")

        # TODO: implementasi penampilan daftar mahasiswa beserta info singkatnya dengan memanggil method infoLine()

    def add_score_to_student(self) -> None:
        # TODO: implement penambahan score ke mahasiswa
        # Hint: minta input nama mahasiswa, cari dengan _find_by_name(), lalu minta input score baru dan tambahkan
        print("✅ Nilai ditambahkan.")

    def edit_student_score(self) -> None:
        # TODO: implement edit score mahasiswa
        name = input("Nama mahasiswa: ").strip()
        s = self._find_by_name(name)
        if not s:
            print("Mahasiswa tidak ditemukan.")
            return
        if not s.scores:
            print("Mahasiswa belum memiliki nilai.")
            return

        for i, sc in enumerate(s.scores):
            print(f"{i}) {sc:.2f}")
        try:
            idx = int(input("Pilih index nilai yang akan diubah: ").strip())
        except ValueError:
            print("Index harus angka.")
            return

        new_raw = input("Nilai baru (0..100): ").strip()
        s.edit_score(idx, self._parse_score(new_raw))
        print("✅ Nilai diperbarui.")

    def delete_student_score(self) -> None:
        # TODO: implement hapus score mahasiswa
        print("🗑️ Nilai dihapus.")

    def edit_student_name(self) -> None:
        # TODO: implement edit nama mahasiswa
        print("✅ Nama mahasiswa diperbarui.")

    def delete_student(self) -> None:
        name = input("Nama mahasiswa yang dihapus: ").strip()
        s = self._find_by_name(name)
        if not s:
            print("Mahasiswa tidak ditemukan.")
            return
        self.students.remove(s)
        print("🗑️ Mahasiswa dihapus.")

    def class_stats(self) -> None:
        if not self.students:
            print("Belum ada data.")
            return
        class_avg = sum(s.average() for s in self.students) / len(self.students)
        top = max(self.students, key=lambda s: s.average())
        print(f"📊 Rata-rata kelas: {class_avg:.2f}")
        print(f"🏆 Top student: {top.name} (avg={top.average():.2f}, grade={top.grade()})")
    def save_json(self) -> None:
        path = input(f"Nama file (default: {DEFAULT_PATH}): ").strip() or DEFAULT_PATH
        save_to_file(self.students, Path(path))
        print(f"💾 Data disimpan ke {path}")
    def load_json(self) -> None:
        path = input(f"Nama file (default: {DEFAULT_PATH}): ").strip() or DEFAULT_PATH
        self.students = load_from_file(Path(path))
        print(f"📂 Data dimuat. Total mahasiswa: {len(self.students)}")
