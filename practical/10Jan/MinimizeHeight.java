package foundation;

import java.util.Arrays;
import java.util.Scanner;

public class MinimizeHeight {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        int k = sc.nextInt();

        findMinHeight(arr, n, k);
    }

    static void findMinHeight(int[] arr, int n, int k){
        Arrays.sort(arr);

        int max = 0, min = 0;
        int ans = arr[n-1] - arr[0];
        int lar = arr[n-1] - k, sml = arr[0] + k;

        for(int i = 0; i < n - 1; i++){
            min = Math.min(sml, arr[i+1] - k);
            max = Math.max(lar, arr[i] + k);
            if(min < 0)
                continue;
            ans = Math.min(ans, max - min);
        }
        System.out.println("Maximum difference is " + ans);

    }
}
//OUTPUT
// 4
// 1 5 15 10
// 3
// Maximum difference is 8
