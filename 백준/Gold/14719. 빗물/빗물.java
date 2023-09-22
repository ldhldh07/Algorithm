import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().split(" ");
        int W = Integer.parseInt(input[1]);

        int[] heights = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] limitHeights = new int[W];

        int limitHeight = 0;

        for (int i=0; i < W; i++) {
            int height = heights[i];
            if (limitHeight < height) {
                limitHeight = height;
            }
            limitHeights[i] = limitHeight;
        }

        limitHeight = 0;

        for (int j=W-1;j >= 0;j--) {
            int height = heights[j];
            if (limitHeight < height) {
                limitHeight = height;
            }
            limitHeights[j] = Math.min(limitHeight, limitHeights[j]);
        }

        int answer = 0;
        for (int w=0; w< W; w++) {
            answer = answer + (limitHeights[w]-heights[w]);
        }
        bw.write(String.valueOf(answer));
        bw.flush();
        br.close();
        bw.close();
    }
}