package clase;
/*
 * amogus
 */
public class clase {
//metodo constructor
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.print("Hola Mundo");
		System.out.println("Mi nombre es Sebastian");
		//tipos de datos primitivos
		int edad=38;
		System.out.print("Mi edad es:"+edad);
		//Decimales
		double estatura=1.7;
		//System.out.printLn(edad);
		System.out.println("Mi estatura es"+estatura+"m.");

		//alfanumérico
		String nombre="Sebastian";
		System.out.println(nombre.getClass().getSimpleName());
		//char - un solo caracter
		char a='s';
		
		//Booleano
		boolean verdad=true;
		
		var flor= "Holitas";
		System.out.println(flor);
		
		final String mail="squiroga585@unab.edu.co";
		System.out.println(mail);
		//mail="comamonda@unab.edu.co";
		System.out.println(mail);
	}

}
