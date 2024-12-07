use std::collections::HashMap;
use std::fs;

const TEST_INPUT: &str = "\
3   4
4   3
2   5
1   3
3   9
3   3
";
const EXPECTED_PART1: i32 = 11;
const EXPECTED_PART2: i32 = 31;

fn read_input_file(file_path: &str) -> String {
    let contents = fs::read_to_string(file_path).unwrap();

    contents
}

fn part1(contents: &str) -> i32 {
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();

    contents.lines().for_each(|line| {
        let parts: Vec<&str> = line.split_whitespace().collect();
        left.push(parts[0].parse::<i32>().unwrap());
        right.push(parts[1].parse::<i32>().unwrap());
    });

    left.sort();
    right.sort();

    let res: i32 = left
        .iter()
        .zip(right)
        .map(|(elem_a, elem_b)| (elem_a - elem_b).abs())
        .sum();

    res
}

fn part2(contents: &str) -> i32 {
    let mut left: Vec<i32> = Vec::new();
    let mut right: HashMap<i32, i32> = HashMap::new();

    contents.lines().for_each(|line| {
        let parts: Vec<&str> = line.split_whitespace().collect();
        left.push(parts[0].parse::<i32>().unwrap());
        right
            .entry(parts[1].parse::<i32>().unwrap())
            .and_modify(|i| *i += 1)
            .or_insert(1);
    });

    let res: i32 = left.iter().map(|x| *x * right.get(x).unwrap_or(&0)).sum();

    res
}

#[cfg(test)]
mod tests {

    use crate::{part1, part2, EXPECTED_PART1, EXPECTED_PART2, TEST_INPUT};

    #[test]
    fn test_part1() {
        let result = part1(&TEST_INPUT);
        assert_eq!(result, EXPECTED_PART1);
    }

    #[test]
    fn test_part2() {
        let result: i32 = part2(&TEST_INPUT);
        assert_eq!(result, EXPECTED_PART2);
    }
}

fn main() {
    let contents = read_input_file("input");

    let answer = part1(&contents);
    println!("{:?}", answer);

    let answer = part2(&contents);
    println!("{:?}", answer)
}
