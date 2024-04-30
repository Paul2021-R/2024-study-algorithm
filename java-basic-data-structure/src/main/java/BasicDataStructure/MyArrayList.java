package BasicDataStructure;

public class MyArrayList<T> {
    private Object[] elements;
    private int size = 0;

    public MyArrayList() {
        this.elements = new Object[10];
    }

    public void add(T element) {
        if (size == elements.length) {
            increaseCapacity();
        }
        elements[size++] = element;
    }

    private void increaseCapacity() {
        Object[] newElements = new Object[elements.length * 2];
        System.arraycopy(elements, 0, newElements, 0, elements.length);
        elements = newElements;
    }

    public int getSize() {
        return size;
    }

    public T get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
        }
        return (T) elements[index];
    }
}
