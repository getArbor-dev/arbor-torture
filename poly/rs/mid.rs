use crate::poly::rs::base::{seed, LIMIT};
pub fn expand(id: usize) -> Vec<usize> { (0..seed(id).min(LIMIT)).collect() }
