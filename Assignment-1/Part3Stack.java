public class Stack {
	private Integer[] arr;
	int size;
	
	public Stack() {
		arr = new Integer[20];
		size = 0;
	}
	
	public void push(Integer newElement) {
		if (size == arr.length) {
			doubleArr();
		}
		arr[size] = newElement;
		size++;
	}
	
	public Integer pop() {
		if (!isEmpty()) {
			Integer poppedElement = arr[size-1];
			size--;
			return poppedElement;
		}
		else {
			return -1;
		}
	}
	
	public Integer top() {
		if (!isEmpty()) {
			return arr[size-1];
		}
		else {
			return -1;
		}
	}
	
	public boolean isEmpty() {
		return size == 0;
	}
	
	public Integer size() {
		return size;
	}
	
	private void doubleArr() {
		Integer[] copyArr = new Integer[arr.length * 2];
		
		for (int i = 0; i < arr.length; i++) {
			copyArr[i] = arr[i];
		}
		arr = copyArr;
	}
}
