package darts

import "math"

//Score returns the score from a point x,y
func Score(x, y float64) int {
	score := 0

	r := math.Hypot(x, y)

	switch {
	case r > 10:
		score = 0
	case r > 5:
		score = 1
	case r > 1:
		score = 5
	case r >= 0:
		score = 10
	}

	return score
}
