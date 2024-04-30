package BasicDataStructure;

import java.util.NoSuchElementException;

public class MyQueue<T> {
    private Node<T> head;
    private Node<T> tail;

    private static class Node<T> {
        private T data;
        private Node<T> next;

        Node(T data) {
            this.data = data;
        }
    }

    public void enqueue(T data) {
        Node<T> node = new Node<>(data);
        if (tail != null) {
            tail.next = node;
        }
        tail = node;
        if (head == null) {
            head = node;
        }
    }

    public T dequeue() {
        if (head == null) throw new NoSuchElementException();
        T data = head.data;
        head = head.next;
        if (head == null) {
            tail = null;
        }
        return data;
    }

    public T peek() {
        if (head == null) throw new NoSuchElementException();
        return head.data;
    }

    public boolean isEmpty() {
        return head == null;
    }
}