package foundation;

import java.util.ArrayList;
import java.util.Scanner;

public class WordPresent {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        ArrayList<String> al = new ArrayList<>();
        for(int i = 0; i < n; i++){
            al.add(sc.next());
        }
        String word = sc.next();
        if(checkWord(word, al)){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
    static boolean checkWord(String word, ArrayList<String> al){

        if(word.length() == 0){
           return true;
        }
        for(int i = 1; i <= word.length(); i++){
            if(al.contains(word.substring(0,i)) && checkWord(word.substring(i),al)){
                return true;
            }
        }
        return false;
    }
}
//OUTPUT
// 12
// i like sam sung samsung mobile ice cream icecream man go mango
// ilikesamsung
// Yes
