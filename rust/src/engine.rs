use crate::config::{threshold_for, MAX_DEPTH};

pub struct Walk { pub depth: usize, pub score: f64 }

pub fn walk(seed: usize) -> Walk {
    let depth = seed.min(MAX_DEPTH);
    Walk { depth, score: threshold_for("medium") * depth as f64 }
}

pub fn is_risky(w: &Walk) -> bool {
    w.score > threshold_for("high")
}
