using System;

public static class ReverseString
{
    public static string Reverse(string input)
    {
        var reversed = string.Empty;
        foreach (var ch in input)
            reversed = ch + reversed;

        return reversed;
    }
}
