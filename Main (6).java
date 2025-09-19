import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> tuplas = new ArrayList<>();
        for (int a = 1; a <= 5; a++) {
            tuplas.add("(" + a + ", " + (a * a) + ")");
        }
        System.out.println("Tuplas: " + tuplas);
    }
}
