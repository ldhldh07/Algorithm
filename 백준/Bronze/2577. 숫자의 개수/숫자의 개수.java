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
        List<Integer> immutableList = Collections.nCopies(10, 0);
        List<Integer> NumberList = new ArrayList<>(immutableList);
        String StringResult = String.valueOf(result);
        for(char ch: StringResult.toCharArray()) {
            int index = Character.getNumericValue(ch);
            int currentCount = NumberList.get(index);
            NumberList.set(index, currentCount + 1);
        }
        for (int count : NumberList) {
            bw.write(count + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}