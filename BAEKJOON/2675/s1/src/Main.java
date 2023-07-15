import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for(int i = 0; i < T; i++) {
            String input = br.readLine();
            String inputData[] = input.split(" ");
            int R = Integer.parseInt(inputData[0]);
            String S = inputData[1];
            for (char ch : S.toCharArray()) {
                for (int ii = 0; ii < R; ii++) {
                    bw.write(String.valueOf(ch));
                }
            }
            bw.newLine();
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
