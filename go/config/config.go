package config

const MaxWorkers = 8
const QueueDepth = 256

func ThresholdFor(kind string) float64 {
	switch kind {
	case "high":
		return 0.8
	case "medium":
		return 0.5
	}
	return 0.2
}
