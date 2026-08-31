//! Rust hub. GROUND TRUTH: 2 modules downstream.

pub const MAX_DEPTH: usize = 12;
pub const MAX_NODES: usize = 100_000;

pub fn threshold_for(kind: &str) -> f64 {
    match kind {
        "high" => 0.8,
        "medium" => 0.5,
        _ => 0.2,
    }
}
