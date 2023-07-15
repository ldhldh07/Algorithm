import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        String input = br.readLine();
        String[] inputStringList = input.split(" ");
        int[] inputIntList = Arrays.stream(inputStringList)
                .mapToInt(Integer::parseInt)
                .toArray();

        int max = -(int) Math.pow(10, 6) - 1;
        int min = (int) Math.pow(10, 6) + 1;
        for(int num : inputIntList) {
            if (num > max) {
                max = num;
            }
            if (num < min) {
                min = num;
            }
        }
        bw.write(String.valueOf(min) + " ");
        bw.write(String.valueOf(max));

        bw.flush();
        br.close();
        bw.close();
    }
}
