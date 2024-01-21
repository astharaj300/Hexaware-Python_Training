package foundation;

import java.util.Scanner;

public class Sequence {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        System.out.println(findTermInSequence(n));
    }
    static String findTermInSequence(int n){

        if( n == 0 ) return "";
        String ans = "1";
        if( n == 1 )
            return ans;
        n = n-1;
        while(n-- > 0) {
            String temp = "" ;
            for(int i = 0 ; i < ans.length() ; i++) {
                Integer cnt = 1;
                while(i < ans.length()-1 && ans.charAt(i) == ans.charAt(i+1)) {
                    cnt++;
                    i++;
                }
                temp += cnt.toString() + ans.charAt(i);
            }
            ans = temp;
        }
        return ans;
    }
}
// OUTPUT
// 3
// 21

// 5
// 111221
