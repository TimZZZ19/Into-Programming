package Examples;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

public class WriteFileExample {
    public static void main(String[] args) throws FileNotFoundException {
        // PrintWriter will create the file (or overwrite if exists)
        PrintWriter writer = new PrintWriter("output.txt");
        
        // Write data
        writer.println("Hello, AP CSA!");
        writer.println("Line 2: " + 42);
        writer.print("No newline here ");
        writer.println("but this ends the line.");
        
        System.out.println();

        // Must close to flush data to disk
        writer.close();
        
        System.out.println("File written successfully.");
    }
}