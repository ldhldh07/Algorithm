import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();
        int num = 1;
        List<String> answerList = new ArrayList<>();

        for (int j = 0; j < n; j++){
            int input = Integer.parseInt(br.readLine());
            while (num <= input) {
                stack.push(num++);
                answerList.add("+");
            }
            if (stack.peek() == input) {
                stack.pop();
                answerList.add("-");
            } else {
                bw.write("NO\n");
                bw.flush();
                bw.close();
                br.close();
                return;
            }
        }

        for (String answer : answerList) {
            bw.write(answer + "\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}