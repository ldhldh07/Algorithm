import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int W = sc.nextInt();
        int N = sc.nextInt();
        int M = sc.nextInt();

        int columnCount = (int) Math.ceil((double) W / (M+1));
        int rowCount = (int) Math.ceil((double) H / (N+1));

        System.out.println(columnCount * rowCount);
    }
}

