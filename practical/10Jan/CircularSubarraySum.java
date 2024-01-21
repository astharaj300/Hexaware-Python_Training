package foundation;

import java.util.Scanner;

public class CircularSubarraySum {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        maxCircularSum(arr, n);
    }

    static void maxCircularSum(int[] arr, int n){
        int res = arr[0];

        for(int i = 0; i < n; i++){
            int curr_max = arr[i];
            int curr_sum = arr[i];

            for(int j = 1; j < n; j++){
                int idx = (i+j) % n;
                curr_sum += arr[idx];
                curr_sum = Math.max(curr_max, curr_sum);
            }
            res = Math.max(res, curr_sum);
        }
        System.out.println("Max sum found " + res);
    }
}
//OUTPUT
//9
//2 1 -5 4 -3 1 -3 4 -1
//Max sum found 6