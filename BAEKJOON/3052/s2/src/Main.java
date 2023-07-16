import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Set<Integer> moduloSet = new HashSet<>();

        for(int i = 0; i < 10; i++) {
            int input = Integer.parseInt(br.readLine());
            int modulo = input % 42;
            moduloSet.add(modulo);
        }
        bw.write(Integer.toString(moduloSet.size()));
        bw.flush();
        br.close();
        br.close();
    }
}