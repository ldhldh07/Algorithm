import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Map<Integer, Integer> moduloCount = new HashMap<>();
        for(int i = 0; i < 10; i++) {
            int input = Integer.parseInt(br.readLine());
            int modulo = input % 42;
            Integer numCount = moduloCount.getOrDefault(modulo, 0);
            moduloCount.put(modulo, numCount + 1);
        }
        bw.write(String.valueOf(moduloCount.size()));
        bw.flush();
        br.close();
        bw.close();
    }
}