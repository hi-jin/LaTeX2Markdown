import java.util.*;
import java.io.*;

public class Java {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        Stack<Character> left = new Stack<>();
        Stack<Character> right = new Stack<>();

        left.push(s.charAt(0));
        for (int i = s.length() - 1; i >= 1; i--) {
            right.push(s.charAt(i));
        }

        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            String cmd = br.readLine();

            if (cmd.equals("prev") && left.size() > 1) {
                right.push(left.pop());
            } else if (cmd.equals("next") && right.size() > 1) {
                left.push(right.pop());
            } else if (cmd.equals("left") && left.size() > 1) {
                left.pop();
            } else if (cmd.equals("right") && right.size() > 1) {
                right.pop();
            }
        }

        System.out.print(left.peek() + " " + right.peek());
    }

}
