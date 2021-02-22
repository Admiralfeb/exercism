package space

// Planet name
type Planet string

// Age calculates age on a planet based upon provided seconds and planet in question.
func Age(seconds float64, planetName Planet) float64 {
	const earthYearinSeconds = 31557600

	earthAge := seconds / earthYearinSeconds

	var planetAge float64

	switch planetName {
	case "Mercury":
		planetAge = earthAge / 0.2408467
	case "Venus":
		planetAge = earthAge / 0.61519726
	case "Earth":
		planetAge = earthAge
	case "Mars":
		planetAge = earthAge / 1.8808158
	case "Jupiter":
		planetAge = earthAge / 11.862615
	case "Saturn":
		planetAge = earthAge / 29.447498
	case "Uranus":
		planetAge = earthAge / 84.016846
	case "Neptune":
		planetAge = earthAge / 164.79132
	default:
	}

	if planetAge != 0 {
		return planetAge
	}
	return -1
}
