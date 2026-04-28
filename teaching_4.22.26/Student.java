public class Student {
    private String firstName;
    private String lastName;
    private int assignment1;
    private int assignment2;
    private int assignment3;
    private int exam;

    // Constructor
    public Student(String firstName, String lastName, int a1, int a2, int a3, int exam) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.assignment1 = a1;
        this.assignment2 = a2;
        this.assignment3 = a3;
        this.exam = exam;
    }

    // Getters (only needed for final score and class average)
    public double computeFinalScore() {
        double assignmentsAvg = (assignment1 + assignment2 + assignment3) / 3.0;
        return 0.6 * assignmentsAvg + 0.40 * exam;
        // Equivalent: 0.6 * assignmentsAvg + 0.4 * exam
    }

    public String getLetterGrade() {
        double score = computeFinalScore();
        if (score >= 90) return "A";
        else if (score >= 80) return "B";
        else if (score >= 70) return "C";
        else if (score >= 60) return "D";
        else return "F";
    }

    public String getLastName() {
        return lastName;
    }

    public String getFirstName() {
        return firstName;
    }

}