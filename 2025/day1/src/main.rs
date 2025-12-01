use std::{fs, ops::Rem};

const TEST_INPUT: &str = "\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
";
const EXPECTED_PART1: i32 = 3;
const EXPECTED_PART2: i32 = 6;

fn read_input_file(file_path: &str) -> String {
    let contents = fs::read_to_string(file_path).unwrap();
    contents
}

fn part1(contents: &str) -> i32 {
    let mut dial = 50;
    let mut count = 0;

    for line in contents.lines() {
        let dir = line.chars().next().unwrap();
        let click = line[1..].parse::<i32>().unwrap();
        let delta = if dir == 'L' { -click } else { click };
        dial = (dial + delta).rem_euclid(100);
        if dial == 0 {
            count += 1;
        }
    }
    count
}

fn part2(contents: &str) -> i32 {
    let mut dial: i32 = 50;
    let mut count: i32 = 0;

    for line in contents.lines() {
        let dir = line.chars().next().unwrap();
        let click = line[1..].parse::<i32>().unwrap();
        let step = if dir == 'L' { -1 } else { 1 };
        for _ in 0..click {
            dial = (dial + step).rem_euclid(100);
            if dial == 0 {
                count += 1;
            }
        }
    }
    count
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_part1() {
        let results: i32 = part1(TEST_INPUT);
        assert_eq!(results, EXPECTED_PART1)
    }

    #[test]
    fn test_part2() {
        let results: i32 = part2(TEST_INPUT);
        assert_eq!(results, EXPECTED_PART2)
    }
}

fn main() {
    let contents = read_input_file("input");

    let answer = part1(&contents);
    println!("{answer}");

    let answer = part2(&contents);
    println!("{answer}");
}
