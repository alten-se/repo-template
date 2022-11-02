/**

# Hash for headers

## Summary
does complicated math

## examples
``` rust
use hello::add_two;

assert_eq!(add_two(3), 5);
```
**/
pub fn add_two(num: i32) -> i32 {
    num + 2
}

pub fn hello() {
    println!("Hello, world")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add_two(2);
        assert_eq!(result, 4);
    }
}
