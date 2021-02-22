using System;

public static class Isogram
{
    public static bool IsIsogram(string word)
    {
        var wordArr = word.ToUpper().ToCharArray();
        Array.Sort(wordArr);
        char previousLetter = '-';
        foreach (var letter in wordArr)
        {
            if (Char.IsLetter(letter))
            {
                if (Char.IsLetter(letter) && letter == previousLetter)
                {
                    return false;
                }
                previousLetter = letter;
            }
        }
        return true;
    }
}
