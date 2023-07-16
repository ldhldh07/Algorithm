import java.io.*;
import java.util.*;

class Node {
    int x;
    int y;

    Node(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
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

        List<Integer> dfsResult = dfs(V, N, adjList);
        List<Integer> bfsResult = bfs(V, N, adjList);

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

    public static List<Integer> bfs(int start, int nodeSize, List<List<Integer>> adjList) {
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[nodeSize + 1];
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

    public static List<Integer> dfs(int start, int nodeSize, List<List<Integer>> adjList) {
        Stack<Integer> stack = new Stack<>();
        boolean[] visited = new boolean[nodeSize +1];
        List<Integer> result = new ArrayList<>();

        stack.push(start);

        while(!stack.isEmpty()) {
            int currentNode = stack.pop();

            if (!visited[currentNode]) {
                visited[currentNode] = true;
                result.add(currentNode);

                for (int i = adjList.get(currentNode).size() - 1; i >= 0; i--) {
                    int nextNode = adjList.get(currentNode).get(i);
                    if (!visited[nextNode]) {
                        stack.push(nextNode);
                    }
                }
            }
        }
        return result;
    }
}