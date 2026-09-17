import java.util.Scanner;
public class firstFile{
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in); //you NEED this for inputs
        /*String test="Alright mateys lets see if this works";
        System.out.println(test);*/

        //this reads text
        System.out.print("What is your name? ");
        String name=scanner.nextLine(); //it reads all of the next line

        //this reads integers
        System.out.print("What is your age? ");
        int age=scanner.nextInt(); //this reads for an integer

        //this reads doubles, or floats
        System.out.print("What is your GPA? ");
        double gpa=scanner.nextDouble();

        //this reads booleans
        System.out.print("True or False (true/false)? ");
        boolean trueOrFalse=scanner.nextBoolean();

        if(name.equals("Daniel")){ //use variable.equals() for strings
            System.out.println("Oh, hello Daniel. We know everything about you already.");
        }
        else if(age==99){ //use python comparison symbols for everything else
            System.out.println("Get out of here, oldy.");
        }
        else if(trueOrFalse){ //use just the name of the variable for booleans
            System.out.println("Ok.");
        }
        else{
            System.out.println("Here is your digital profile:");
            System.out.println("Name: "+name);
            System.out.println("Age: "+age);
            System.out.println("GPA: "+gpa);
        }
    }
}