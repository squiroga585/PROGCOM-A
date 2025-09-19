import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> lenguaje = Arrays.asList("pytho", "java", "c++");
        List<String> mayúsculas = new ArrayList<>();
        for (String l : lenguaje) {
            mayúsculas.add(l.toUpperCase());
        }
        System.out.println("Palabras en mayúsculas: " + mayúsculas);
    }
}