import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] numArray = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        boolean isAscending = numArray[0] < numArray[1];
        String answer = isAscending ? "ascending" : "descending";
        for(int i = 2; i < 8; i++) {
            if (numArray[i-1] < numArray[i] != isAscending) {
                answer = "mixed";
            }
        }
        bw.write(answer);
        bw.flush();
        br.close();
        bw.close();
    }
}