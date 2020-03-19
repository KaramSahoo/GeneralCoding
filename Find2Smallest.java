public class find2smallest {

	static void search(int arr[]) { 
		int first, second, len = arr.length;
		if(len<2) {
			System.out.println("Invalid Input!!");
			return;
		}

		first = second = Integer.MAX_VALUE;
		for(int i = 0; i < len; i++) {
			if(arr[i] < first) {
				second = first;
				first = arr[i];
			}
			else if(arr[i] < second & arr[i] != first)
				second = arr[i];
		}
		if(second == Integer.MAX_VALUE)
			System.out.println("Second smallest doest not exist");
		else{
			System.out.println("Smallest number : " + first);
			System.out.println("Second smallest number : " + second);
		}
	}

	public static void main(String[] args) {
		int arr[] = {1,6,4,9,8,5,7};
		search(arr);
	}
}
