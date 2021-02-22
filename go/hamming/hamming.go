//Package hamming checks the hamming distance
package hamming

import (
	"fmt"
)

//Distance compares two strings returning the Hamming distance or an error.
func Distance(a, b string) (int, error) {
	ar, br := []rune(a), []rune(b)

	if len(ar) != len(br) {
		return 0, fmt.Errorf("the DNA strings '%s' and '%s' are not the same length", a, b)
	}

	differences := 0

	for i := range ar {
		if ar[i] != br[i] {
			differences++
		}
	}

	return differences, nil

}
