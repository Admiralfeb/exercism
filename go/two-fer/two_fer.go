package twofer

import "fmt"

// ShareWith you or a name
func ShareWith(name string) string {
	if name == "" {
		name = "you"
	}
	str := fmt.Sprintf("One for %v, one for me.", name)
	return str
}
