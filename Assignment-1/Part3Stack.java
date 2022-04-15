package part3;

public class Stack<T> {
	private Integer[] arr;
	private Integer[] minValArr;
	private int size;
	private int minSize;
	
	public Stack() {
		arr = new Integer[20];
		minValArr = new Integer[20];
		size = 0;
		minSize = 0;
	}
	
	public Integer min() {
		if (!isEmpty()) {
			return minValArr[minSize-1];
		}
		else {
			return -1;
		}
	}
	
	public void push(Integer newElement) {
		if (size == arr.length) {
			arr = doubleArr(arr);
		}
				
		if (minSize == 0 || newElement <= minValArr[minSize-1]) {
			if (minSize == minValArr.length) {
				minValArr = doubleArr(minValArr);
			}
			minValArr[minSize] = newElement;
			minSize++;
		}
		
		arr[size] = newElement;
		size++;
	}
	
	public Integer pop() {
		if (!isEmpty()) {
			size--;
			Integer poppedElement = arr[size];
			if (poppedElement == minValArr[minSize-1]) {
				minSize--;
			}
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
	
	private Integer[] doubleArr(Integer[] doubledArr) {
		Integer[] copyArr = new Integer[doubledArr.length * 2];
		
		for (int i = 0; i < doubledArr.length; i++) {
			copyArr[i] = doubledArr[i];
		}

		return copyArr;
	}
}
