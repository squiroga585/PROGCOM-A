import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<Integer> par = new ArrayList<>();
        for (int z = 0; z <= 20; z++) {
            if (z % 2 == 0) {
                par.add(z);
            }
        }
        System.out.println("Números pares del 0 al 20: " + par);
    }
}