import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class StudentScores {
    public static void main(String[] args) {
        // TODO: Membuat HashMap untuk menyimpan pasangan nama-nilai
        Scanner input = new Scanner(System.in);

        System.out.println("=== Input Data Nilai Mahasiswa ===");

        // Loop input data mahasiswa
        while (true) {
            System.out.print("Masukkan nama (atau kosong untuk selesai): ");
            String name = input.nextLine().trim();
            
            // Jika kosong, hentikan input
            if (name.isEmpty()) break;

            System.out.print("Masukkan nilai: ");
            int score = Integer.parseInt(input.nextLine().trim());

            // TODO: Simpan data (name,score) ke dalam HashMap
        }

        System.out.println("\n=== Daftar Nilai Mahasiswa ===");
        // TODO: Menampilkan semua data dari HashMap

        input.close();
    }
}
