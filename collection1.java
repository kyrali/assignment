package collection;


public class collection1 {

	public collection1() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		System.out.print("surname start with P:\n");
		collection2 c1 =new collection2();
		
		c1.addItem("Plll");
		c1.addItem("Paaa");
		c1.addItem("Alll");
		
		while (c1.hasNext()==true) {
			String surname = c1.getNext();
			String s1= surname.substring(0, 1);
			String s2= "P";
			if (s2.equals(s1)) {
				System.out.print(surname+"\n");
				}
			
		}
		
		
		
		
		
		
		
			
		

	}

}
