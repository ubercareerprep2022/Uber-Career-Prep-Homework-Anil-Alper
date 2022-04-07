package part3;

public class Queue {
	private int rear;
	private int front;
	private int size;
	private Integer queueArr[];
	
	public Queue() {
		rear = -1;
		front = 0;
		size = 0;
		queueArr = new Integer[20];
	}
	
	public void enqueue(Integer newElement) {
		if (size == queueArr.length) {
			doubleArr();
		}
		rear = increment(rear);
		size++;
		queueArr[rear] = newElement;
		
	}
	
	public Integer dequeue() {
		if (!isEmpty()) {
			Integer frontElement = queueArr[front];
			front = increment(front);
			size--;
			return frontElement;
		}
		else {
			return -1;
		}
	}
	
	public Integer rear() {
		if (!isEmpty()) {
			return queueArr[rear];
		}
		else {
			return -1;
		}
	}
	
	public Integer front() {
		if (!isEmpty()) {
			return queueArr[front];
		}
		else {
			return -1;
		}
	}
	
	public Integer size() {
		return size;
	}
	
	public boolean isEmpty() {
		return size == 0;
	}
	
	private Integer increment(int index) {
		if (++index == queueArr.length) {
			return 0;
		}
		else {
			return index;
		}
	}
	
	private void doubleArr() {
		Integer[] copyArr = new Integer[queueArr.length * 2];
		
		for (int i = 0; i < size; i++) {
			copyArr[i] = queueArr[front];
			front = increment(front);
		}
		queueArr = copyArr;
		rear = size-1;
		front = 0;
	}
} 
