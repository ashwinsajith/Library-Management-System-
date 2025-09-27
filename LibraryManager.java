import java.util.Scanner;

public class LibraryManager {


    public static String promptISBN(Scanner sc){
        System.out.print("Enter your input:");
        String input=sc.nextLine();
        String normalizedString=normalizeISBN(input);
        while (true){
            if ((normalizedString.length()==10 || normalizedString.length()==13) && (!normalizedString.isEmpty())){
                break;
            }else{
                System.out.println("Your input is invalid. Try again.");
                System.out.print("Enter your input:");
                input=sc.nextLine();
                normalizedString=normalizeISBN(input);
            }
        }
        return normalizedString;
    }
}
