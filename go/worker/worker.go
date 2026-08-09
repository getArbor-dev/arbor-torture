package worker

import "torture/config"

type Job struct {
	ID    int
	Score float64
}

func Process(j Job) bool {
	return j.Score > config.ThresholdFor("high")
}

func Capacity() int {
	return config.MaxWorkers * 2
}
