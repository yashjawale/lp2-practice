import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MD5Hash {

    // Function to calculate the MD5 hash of a string
    public static String calculateMD5(String input) {
        try {
            // Create a MessageDigest object for MD5
            MessageDigest md = MessageDigest.getInstance("MD5");

            // Update the digest with the input bytes
            md.update(input.getBytes());

            // Compute the MD5 hash
            byte[] digest = md.digest();

            // Convert the byte array to a hexadecimal string
            StringBuilder result = new StringBuilder();
            for (byte b : digest) {
                result.append(String.format("%02x", b));
            }
            return result.toString();
        } catch (NoSuchAlgorithmException e) {
            // Handle NoSuchAlgorithmException
            e.printStackTrace();
            return null;
        }
    }

    // Main method
    public static void main(String[] args) {
        // Example string
        String input = "Hello, MD5!";

        // Calculate the MD5 hash of the input string
        String md5Hash = calculateMD5(input);

        System.out.println("MD5 Hash: " + md5Hash);
    }
}
