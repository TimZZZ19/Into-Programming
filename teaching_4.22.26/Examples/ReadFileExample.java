package Examples;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadFileExample {
    public static void main(String[] args) throws FileNotFoundException {
        // Create a File object with the path to the text file
        File inputFile = new File("data.txt");
        
        // Open the file using a Scanner
        Scanner fileScanner = new Scanner(inputFile);
        
        // Read line by line and print to console
        while (fileScanner.hasNextLine()) {
            String line = fileScanner.nextLine();
            System.out.println(line);
        }
        
        // Close the scanner to free system resources
        fileScanner.close();
    }
}
