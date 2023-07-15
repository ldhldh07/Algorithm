import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int max = 0;
        int IndexOfMax = -1;

        for (int i = 1; i<= 9; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num > max) {
                max = num;
                IndexOfMax = i;
            }
        }
        bw.write(String.valueOf(max));
        bw.newLine();
        bw.write(String.valueOf(IndexOfMax));
        bw.flush();
        bw.close();
        br.close();
    }
}