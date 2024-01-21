package foundation;

import java.util.Scanner;

public class FindSumPair {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        int sum = sc.nextInt();

        findPairSum(arr,sum);
    }
    static void findPairSum(int[] arr, int sum){

        int flag = 0;
        for(int i = 0; i < arr.length; i++){
            for(int j = i+1; j < arr.length; j++){
                if(arr[i] + arr[j] == sum){
                    flag = 1;
                    System.out.println("Pair found ("+ arr[i] + " ,"+ arr[j]+")");
                    break;
                }
            }
            if(flag == 1){
                break;
            }
        }
    }
}
// OUTPUT
//    6
//    8 7 2 5 3 1
//    10
//    Pair found (8 ,2)

