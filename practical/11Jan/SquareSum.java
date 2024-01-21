package foundation;

import java.util.Scanner;

public class SquareSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(findMinSquareSum(n));
    }
    static int findMinSquareSum(int n){
        //Recursive
//            if(n < 4){
//                return n;
//            }
//
//        int res = n;
//        for (int i = 1; i <= n; i++) {
//            int temp = i * i;
//            if (temp > n)
//                break;
//            else
//                res = Math.min(res, 1 + findMinSquareSum(n - temp));
//        }
//        return res;
        // Tabulation (Bottom Up DP)
        int[] dp = new int[n + 1];
        dp[0] = 0;

        for (int i = 1; i <= n; i++) {
            dp[i] = i;

            for (int j = 1; j * j <= i; j++) {
                int square = j * j;
                dp[i] = Math.min(dp[i], 1 + dp[i - square]);
            }
        }

        return dp[n];
    }
}
//OUTPUT
// 6(input)
// 3

// 100(input)
// 1
