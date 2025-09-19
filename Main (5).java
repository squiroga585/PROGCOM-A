import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> lista = new ArrayList<>();
        for (int z = 1; z <= 10; z++) {
            if (z % 2 == 0) {
                lista.add(z + "es par");
            } else {
                lista.add(z + "es impar");
            }
        }
        System.out.println("impar o par: " + lista);
    }
}