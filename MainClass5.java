class Central1
{
	int j=33;
	static double p=22.53;
}
class MainClass5
{
	static void test()
	{
		System.out.println("TEST METHOD");
	}
	public static void main(String[] args)
	{
		System.out.println("MAIN METHOD");
		test();
		Central1 c1 = new Central1();
		System.out.println(" J VALUE IS: "+c1.j);
	}	
}	

