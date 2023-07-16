import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inputs = br.readLine().split(" ");
        int N = Integer.parseInt(inputs[0]);
        int M = Integer.parseInt(inputs[1]);
        int V = Integer.parseInt(inputs[2]);

        List<List<Integer>> adjList = new ArrayList<>();
        for (int j = 0; j < N+1; j ++) {
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            String[] nodeInput = br.readLine().split(" ");
            int start = Integer.parseInt(nodeInput[0]);
            int end = Integer.parseInt(nodeInput[1]);
            adjList.get(start).add(end);
            adjList.get(end).add(start);
        }

        for (List<Integer> list : adjList) {
            Collections.sort(list);
        }

        boolean[] visited = new boolean[N+1];
        List<Integer> dfsResult = new ArrayList<>();
        dfs(V, visited, dfsResult, adjList);

        visited = new boolean[N+1];
        List<Integer> bfsResult = bfs(V, N, adjList, visited);

        for (int dfsRes : dfsResult) {
            bw.write(String.valueOf(dfsRes) + " ");
        }
        bw.newLine();
        for (int bfsRes: bfsResult) {
            bw.write(String.valueOf(bfsRes)+ " ");
        }
        bw.flush();
        br.close();
        bw.close();

    }

    public static void dfs(int current, boolean[] visited, List<Integer> result, List<List<Integer>> adjList) {
        visited[current] = true;
        result.add(current);

        for (int next : adjList.get(current)) {
            if (!visited[next]) {
                dfs(next, visited, result, adjList);
            }
        }
    }

    public static List<Integer> bfs(int start, int nodeSize, List<List<Integer>> adjList, boolean[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        List<Integer> result = new ArrayList<>();

        queue.add(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int currentNode = queue.poll();
            result.add(currentNode);

            for (int nextNode : adjList.get(currentNode)) {
                if (!visited[nextNode]) {
                    queue.add(nextNode);
                    visited[nextNode] = true;
                }
            }
        }

        return result;
    }
}