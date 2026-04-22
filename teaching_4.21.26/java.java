// 26年新增知识点：文件读写 File I/O
// Combine Read and Write:
import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class CopyFileExample {
	public static void main(String[] args) throws FileNotFoundException{ //一定要记得写Exception
		File source = new File("original.txt");
		Scanner reader = new Scanner(source);
		
		PrintWriter writer = new PrintWriter("copy.txt");
		
		while (reader.hasNextLine()){
			String line = reader.nextLine();
			writer.println(line);
		}

		reader.close();
		writer.close(); //一定要记得close
	}

}

