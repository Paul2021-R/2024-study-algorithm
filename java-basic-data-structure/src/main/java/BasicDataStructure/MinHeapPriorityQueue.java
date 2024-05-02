package BasicDataStructure;

public class MinHeapPriorityQueue {
    private int[] heap;
    private int size;
    private int capacity;

    public MinHeapPriorityQueue(int capacity) {
        this.capacity = capacity;
        this.heap = new int[capacity + 1];
        this.size = 0;
        heap[0] = Integer.MIN_VALUE; // 힙의 가장 앞에 최소값 설정
    }

    private int parent(int pos) { return pos / 2; }
    private int leftChild(int pos) { return (2 * pos); }
    private int rightChild(int pos) { return (2 * pos + 1); }
    private boolean isLeaf(int pos) { return pos > (size / 2) && pos <= size; }

    private void swap(int fpos, int spos) {
        int tmp = heap[fpos];
        heap[fpos] = heap[spos];
        heap[spos] = tmp;
    }

    public void insert(int element) {
        if (size >= capacity) {
            return; // 힙이 꽉 찼을 경우
        }
        heap[++size] = element;
        int current = size;

        while (heap[current] < heap[parent(current)]) {
            swap(current, parent(current));
            current = parent(current);
        }
    }

    public int remove() {
        int popped = heap[1];
        heap[1] = heap[size--];
        minHeapify(1);
        return popped;
    }

    private void minHeapify(int pos) {
        if (!isLeaf(pos)) {
            if (heap[pos] > heap[leftChild(pos)] || heap[pos] > heap[rightChild(pos)]) {
                if (heap[leftChild(pos)] < heap[rightChild(pos)]) {
                    swap(pos, leftChild(pos));
                    minHeapify(leftChild(pos));
                } else {
                    swap(pos, rightChild(pos));
                    minHeapify(rightChild(pos));
                }
            }
        }
    }

    public static void main(String[] args) {
        MinHeapPriorityQueue minHeap = new MinHeapPriorityQueue(15);
        minHeap.insert(5);
        minHeap.insert(3);
        minHeap.insert(17);
        minHeap.insert(10);
        minHeap.insert(84);
        minHeap.insert(19);
        minHeap.insert(6);
        minHeap.insert(22);
        minHeap.insert(9);

        System.out.println("The Min-Val is: " + minHeap.remove());
        System.out.println("The Min-Val is: " + minHeap.remove());
        System.out.println("The Min-Val is: " + minHeap.remove());
        System.out.println("The Min-Val is: " + minHeap.remove());
    }
}