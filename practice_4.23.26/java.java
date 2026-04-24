public class java {
    public static void main(String[] args){
        System.out.println("hello");
        int[] arr = {1, 2, 3, 4, 5};
        for(int i = 0; i < arr.length; i++) {
            System.out.println(i);           
        }
        
        int currMin = -1;
        System.out.println("Hello");
        for(int i = 0; i < arr.length; i++){
        	if(currMin < arr[i]){
        	    currMin = arr[i];
         	}
        }
    }
}	