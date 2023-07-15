import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int result = 1;
        for(int i = 0; i < 3; i++) {
            result = result * Integer.parseInt(br.readLine());
        }
        String stringResult = String.valueOf(result);
        int[] countList = new int[10];
        for (int i = 0; i < stringResult.length(); i++) {
            countList[stringResult.charAt(i) - '0']++;
        }
        for (int count : countList) {
            bw.write(String.valueOf(count));
            bw.newLine();
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
