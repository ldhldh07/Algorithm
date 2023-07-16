import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<String, Integer> nameIndex = new HashMap<>();
        String[] indexName = new String[N + 1];

        for (int i = 1; i < N+1; i++) {
            String name = br.readLine();
            nameIndex.put(name, i);
            indexName[i] = name;
        }

        StringBuilder sb = new StringBuilder();
        for (int j = 0; j < M; j++) {
            String mInput = br.readLine();
            if (isDigit(mInput)) {
                sb.append(indexName[Integer.parseInt(mInput)]).append("\n");
            } else {
                sb.append(nameIndex.get(mInput)).append("\n");
            }
        }
        bw.write(sb.toString());
        bw.flush();
        br.close();
        bw.close();
    }

    public static boolean isDigit (String input) {
        try {
            Integer.parseInt(input);
            return true;
        } catch(NumberFormatException error) {
            return false;
        }
    }
}