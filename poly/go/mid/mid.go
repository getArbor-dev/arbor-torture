package mid

import "torture/poly/go/base"

func Expand(id int) []int {
	n := base.Seed(id)
	if n > base.Limit { n = base.Limit }
	out := make([]int, n)
	return out
}
