package foundation;

import java.util.Scanner;

public class DivisibleBy7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if(checkDivisible(n)){
            System.out.println("No. is divisible by 7");
        }
        else{
            System.out.println("Not divisible by 7");
        }
    }
    static boolean checkDivisible(int n){

        if(n < 0){
           return checkDivisible(-n);
        }
        if(n == 0 || n== 7){
            return true;
        }
        if(n < 10){
            return false;
        }
        return checkDivisible(n/10 - 2 * (n - (n/10) * 10));
    }
}
//OUTPUT
//371
//No. is divisible by 7

//15
//Not divisible by 7