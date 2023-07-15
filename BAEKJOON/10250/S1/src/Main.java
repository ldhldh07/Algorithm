import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            String input = br.readLine();
            String[] data = input.split(" ");
            int H = Integer.parseInt(data[0]);
            int W = Integer.parseInt(data[1]);
            int N = Integer.parseInt(data[2]);

            int floor = (N % H == 0) ? H : N % H;
            int number = (N % H == 0) ? N / H : N / H + 1;
            int answer = 100 * floor + number;

            bw.write(String.valueOf(answer));
            bw.newLine();
        }
        bw.flush();
        br.close();
        bw.close();

    }
}
