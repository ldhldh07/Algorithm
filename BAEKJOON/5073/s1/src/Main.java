import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while (true) {
            String[] inputs = br.readLine().split(" ");
            if ("0".equals(inputs[0]) && "0".equals(inputs[1]) && "0".equals(inputs[2])) {
                break;
            }

            List<Integer> inputList = Arrays.stream(inputs)
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());

            int sumOfList = inputList.stream().mapToInt(Integer::intValue).sum();
            int maxOfList = inputList.stream().mapToInt(Integer::intValue).max().getAsInt();

            if (maxOfList >= sumOfList - maxOfList) {
                bw.write("Invalid");
                bw.newLine();
                continue;
            }

            Set<Integer> inputSet = new HashSet<>(inputList);
            int setLength = inputSet.size();

            switch (setLength) {
                case 1:
                    bw.write("Equilateral");
                    break;
                case 2:
                    bw.write("Isosceles");
                    break;
                case 3:
                    bw.write("Scalene");
                    break;
            }
            bw.newLine();
        }
        bw.flush();
        br.close();
        bw.close();
    }
}