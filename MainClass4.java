class MainClass4
{
	static int k=12;
	double d = 33.66;
	
	static void test()
	{
		System.out.println("TEST METHOD");
	}
	void display()
	{
		System.out.println("DISPLAY METHOD");
		
	}
	public static void main(String[] args)
	{
		System.out.println("K VALUE IS: "+k);
		test();
		MainClass4 m4 = new MainClass4();
		System.out.println("D VALUE IS: " +m4.d);
		m4.display();
	
	}
	
}
