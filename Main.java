import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Integer> cuadra = new ArrayList<>();
        for (int x = 1; x <= 10; x++) {
            cuadra.add(x * x);
        }
        System.out.println("Cuadrados del 1 al 10: " + cuadra);
    }
}