use crate::engine::{is_risky, walk, Walk};

pub fn summarize(seed: usize) -> String {
    let w: Walk = walk(seed);
    if is_risky(&w) {
        format!("HIGH depth={} score={:.2}", w.depth, w.score)
    } else {
        format!("ok depth={} score={:.2}", w.depth, w.score)
    }
}
