import java.util.*;

public class Main {
    public static void main(String[] args) {
        String palabra = "programacion";
        ArrayList<Character> vocal = new ArrayList<>();
        for (int x = 0; x < palabra.length(); x++) {
            char c = palabra.charAt(x);
            if ("aeiou".indexOf(c) != -1) {
                vocal.add(c);
            }
        }
        System.out.println("vocales en la palabra (programacion):");
        System.out.println(vocal);
    }
}