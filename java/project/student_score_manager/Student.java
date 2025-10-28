import java.util.ArrayList;
import java.util.List;

public class Student {
    private String name;
    private ArrayList<Double> scores;

    public Student(String name) {
        this.name = name;
        this.scores = new ArrayList<>();
    }

    public String getName() { return name; }
    public void setName(String newName) { this.name = newName; }

    public List<Double> getScores() { return scores; }

    public void addScore(double score) {
        // TODO: add score dengan validasi 0..100
    }

    public void editScore(int index, double newScore) {
        if (index < 0 || index >= scores.size()) throw new IndexOutOfBoundsException("Index nilai tidak valid");
        if (newScore < 0 || newScore > 100) throw new IllegalArgumentException("Score harus 0..100");
        // TODO: edit score dengan specific index
    }

    public void removeScore(int index) {
        if (index < 0 || index >= scores.size()) throw new IndexOutOfBoundsException("Index nilai tidak valid");
        // TODO: hapus score dengan specific index
    }

    public double getAverage() {
        // TODO: hitung rata-rata dari scores ArrayList, kembalikan 0 jika belum ada nilai
        return 0.0;
    }

    public String getGrade() {
        double avg = getAverage();
        // TODO: kembalikan grade berdasarkan kondisi average
        return "E";
    }

    // TODO: buat fungsi infoLine() yang return string dengan format:
    // Nama | scores=[..] | avg=.. | grade=..
}
