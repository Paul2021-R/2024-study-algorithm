package BasicDataStructure;

import java.util.*;

public class BFS {
    private int V;
    private LinkedList<Integer> adj[];

    public BFS(int v) {
        this.V = v;
        adj = new LinkedList[v];
        for (int i = 0; i < this.V; ++i) {
            adj[i] = new LinkedList();
        }
    }

    void addEdge(int v, int w) {
        adj[v].add(w); // 노드 v에 인접한 노드 w 추가
    }

    void BFS(int s) {
        boolean visited[] = new boolean[this.V];
        LinkedList<Integer> queue = new LinkedList<Integer>();

        visited[s] = true;
        queue.add(s);

        while(queue.size() != 0) {
            s = queue.poll(); // 원소 하나 제거하고 반환
            System.out.print(s + " ");

            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext()) {
                int n = i.next();
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }

    public static void main(String args[]) {
        BFS g = new BFS(4);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        System.out.println("Breadth First Traversal (starting from vertex 2)");

        g.BFS(2);
    }
}