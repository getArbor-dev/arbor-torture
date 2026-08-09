package handler

import "torture/poly/go/mid"

func HandleRequest(id int) int { return len(mid.Expand(id)) }
