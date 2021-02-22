//Package proverb works to generate a proverb
package proverb

import "fmt"

// Proverb should have a comment documenting it.
func Proverb(rhyme []string) (final []string) {
	final = make([]string, 0)

	if len(rhyme) == 0 {
		return []string{}
	}
	if len(rhyme) > 1 {
		for i := 0; i < len(rhyme)-1; i++ {
			if i >= len(rhyme)-1 {
				break
			}
			final = append(final, buildContinuationLine(rhyme[i], rhyme[i+1]))
		}
	}
	final = append(final, buildLastLine(rhyme[0]))
	return
}

func buildContinuationLine(s1, s2 string) string {
	return fmt.Sprintf("For want of a %s the %s was lost.", s1, s2)
}

func buildLastLine(s string) string {
	return fmt.Sprintf("And all for the want of a %s.", s)
}
