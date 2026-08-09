use crate::poly::rs::mid::expand;
pub fn handle_request(id: usize) -> usize { expand(id).len() }
