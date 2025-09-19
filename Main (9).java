public class Main {
    public static void main(String[] args) {
        int[] temperaturas = {22, 25, 27, 29, 30, 33};

        for (int temp : temperaturas) {
            if (temp < 26) {
                System.out.println(temp + "°C ’ frio");
            } else if (temp <= 29) {
                System.out.println(temp + "°C ’ templado");
            } else {
                System.out.println(temp + "°C ’ caliente");
            }
        }
    }
}