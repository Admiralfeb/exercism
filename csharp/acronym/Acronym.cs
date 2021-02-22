using System;

public static class Acronym
{
    public static string Abbreviate(string phrase)
    {
        var abbr = string.Empty;
        var delimiters = new char[] { ' ', '-', '_' };

        foreach (var word in phrase.Split(delimiters, StringSplitOptions.RemoveEmptyEntries))
        {
            abbr += word[0].ToString().ToUpper();
        }

        return abbr;
    }
}
