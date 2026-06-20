public class Main {
    public static void main(String[] args) {
        int start[] = {1, 3, 0, 5, 8, 5};
        int end[]   = {2, 4, 6, 7, 9, 9};
        System.out.println("Selected Activities:");
        // first activity
        int i = 0;
        System.out.println(start[i] + " " + end[i]);
        // remaining activities
        for (int j = 1; j < start.length; j++) {
            if (start[j] >= end[i]) {
                System.out.println(start[j] + " " + end[j]);
                i = j;
            }
        }
    }
}