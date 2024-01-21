package foundation;

import java.util.Scanner;

public class ReplaceWithProduct {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int [] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        replaceWithProduct(arr, n);
    }
    static void replaceWithProduct(int[] arr, int n){
        int []left_pro =  new int[n];
        int [] right_pro = new int[n];

        int[] ans = new int[n];

        int left = 1;
        int right = 1;

        for(int i = 0; i < n; i++){
            left_pro[i] = left;
            left *= arr[i];

            right_pro[n-1-i] = right;
            right *= arr[n-1-i];

        }

        for(int i = 0; i < n; i++){
            ans[i] = left_pro[i] * right_pro[i];
        }

        for(int i = 0; i < n; i++){
            System.out.print(ans[i] + " ");
        }
    }
}
//OUTPUT
//        5
//        1 2 3 4 5
//        120 60 40 30 24