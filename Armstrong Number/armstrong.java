import java.util.*;
class armstrong
{
	public static void main(String[] Args)
	{
		Scanner Sc=new Scanner(System.in);
		int n=Sc.nextInt();
		int t=n,r,s=0;
		while(t>0)
		{
			r=t%10;
			s=s+r*r*r;
			t=t/10;
		}
		if(s==n)
			System.out.println("armstrong");
		else
			System.out.println("not armstrong");
	}
}