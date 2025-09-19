import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> palabras = Arrays.asList("sol", "estrella", "mar", "planeta");
        List<String> resultado = new ArrayList<>();

        for (String p : palabras) {
            if (p.length() > 4) {
                resultado.add(p);
            }
        }

        System.out.println("Palabras con más de 4 letras: " + resultado);
    }
}