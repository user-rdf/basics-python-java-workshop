public class OddChecker {

    // TODO: Method 1: Mengecek apakah sebuah angka ganjil
    public static boolean is_odd(int num) {
        return false;
    }

    // TODO: Method 2 (Overloading): Mengecek apakah elemen array pada index tertentu ganjil
    // input: array of int, dan index

    // Method main untuk pengujian
    public static void main(String[] args) {
        System.out.println(is_odd(7));            // true  → 7 ganjil
        System.out.println(is_odd(10));           // false → 10 genap

        int[] numbers = {2, 5, 8, 11};
        // System.out.println(is_odd(numbers, 1));   // true  → arr[1] = 5
        // System.out.println(is_odd(numbers, 2));   // false → arr[2] = 8
        // System.out.println(is_odd(numbers, 5));   // cetak "Index di luar batas array!"
    }
}
