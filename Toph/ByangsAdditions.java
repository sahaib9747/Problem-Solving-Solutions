import java.util.*;

public class Solution {
    
    public static void main(String[] args) {
        
		//scanner
		Scanner sc = new Scanner(System.in);
		
		//inputs
        String a = sc.next();
        String b = sc.next();
		
		//calculations
		boolean v = false;
		int x;
		int la = a.length();
		int lb = b.length();
        int min = Math.min(la, lb);
		
		//loop
		for (int i = 1; i <= min; ++i) {
			x = Character.getNumericValue( a.charAt(la-i) ) + Character.getNumericValue( b.charAt(lb-i) );
			if (x > 9) {
				v = true;
				break;
			}
		}
		
		//results
		if (v) System.out.println("Yes");
		else System.out.println("No");
		
    }
    
}