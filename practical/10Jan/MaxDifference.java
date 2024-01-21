package foundation;

import java.util.Scanner;

public class MaxDifference {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        findMaxDiff(arr, n);
    }
    static void findMaxDiff(int[] arr, int n){
        int maxDiff = arr[1]- arr[0];
        int minVal = arr[0];

        for(int j = 1; j < n; j++){
            int curr_max = arr[j] - minVal;
            maxDiff = Math.max(maxDiff,curr_max);
            minVal = Math.min(minVal, arr[j]);

        }
        System.out.println("The maximum difference is " + maxDiff );

    }
}
//OUTPUT
//  7
//  2 7 9 5 1 3 5
//  The maximum difference is 7
