public class Encryption
{
    public static void main(String[] args)
    {
        String msg = "you're cute";
        String encryptedMsg = encrypt(msg, 5);

        System.out.println(encryptedMsg);

        String decryptedMsg = decrypt(encryptedMsg, 5);
        System.out.println(decryptedMsg);
    }

    static String encrypt(String message, int shift)
    {
        String test = "";
        for(int i = 0; i < message.length(); i++)
        {
            test += (char)(message.charAt(i) + shift);
        }
        return test;
    }

    static String decrypt(String message, int shift)
    {
        String test = "";
        for(int i = 0; i < message.length(); i++)
        {
            test += (char)(message.charAt(i) - shift);
        }
        return test;
    }

    static String symmetricEncypt(String message, String key)
    {
        return message;
    }
}