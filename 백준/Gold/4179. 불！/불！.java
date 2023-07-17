import java.io.*;
import java.util.*;

public class Main {

    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        char[][] miro = new char[R][C];
        for (int i = 0; i < R; i ++) {
            miro[i] = br.readLine().toCharArray();
        }
        Node start = null;
        Queue<Node> fires = new LinkedList<Node>();

        for (int y=0; y < R; y++) {
            for (int x=0; x < C; x++) {
                if (miro[y][x] == 'J') {
                    start = new Node(y, x);
                } else if (miro[y][x] == 'F'){
                    fires.add(new Node(y, x));
                }
            }
        }

        int result = bfs(start, fires, R, C, miro);
        bw.write(result == -1 ? "IMPOSSIBLE" :  String.valueOf(result));
        bw.flush();
        br.close();
        bw.close();
    }

    static class Node {
        int a;
        int b;
        Node(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }

    static int bfs(Node startPoint, Queue<Node> fires, int R, int C, char[][] miro) {

        Queue<Node> queue = new LinkedList<Node>();
        queue.add(startPoint);

        int[][] visited = new int[R][C];
        visited[startPoint.a][startPoint.b] = 1;

        int[][] fireVisited = new int[R][C];

        for (Node fire : fires) {
            fireVisited[fire.a][fire.b] = 1;
        }

        while(!queue.isEmpty()) {
            int fireSize = fires.size();
            for (int i=0; i < fireSize; i++) {
                Node currentFire = fires.poll();
                for(int t = 0; t < 4; t++) {
                    int nfi = currentFire.a + di[t];
                    int nfj = currentFire.b + dj[t];
                    if (nfi >= 0 && nfi < R && nfj >=0 && nfj < C && miro[nfi][nfj] == '.' && fireVisited[nfi][nfj] == 0) {
                        fires.add(new Node(nfi, nfj));
                        fireVisited[nfi][nfj] = fireVisited[currentFire.a][currentFire.b] + 1;
                    }
                }
            }
            int size = queue.size();
            for (int i =0; i < size; i++) {
                Node currentPoint = queue.poll();
                int ci = currentPoint.a;
                int cj = currentPoint.b;

                for (int t = 0; t < 4; t++) {
                    int ni = ci + di[t];
                    int nj = cj + dj[t];

                    if (ni < 0 || ni >= R || nj < 0 || nj >= C) {
                        return visited[ci][cj];
                    }
                    if (miro[ni][nj] == '.' && visited[ni][nj] == 0 && (fireVisited[ni][nj] == 0 || visited[ci][cj] + 1 < fireVisited[ni][nj])) {
                        queue.add(new Node(ni, nj));
                        visited[ni][nj] = visited[ci][cj] + 1;
                    }
                }
            }
        }
        return -1;
    }

}