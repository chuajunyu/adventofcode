use aoc2025::read_file;

fn main() {
    let file_path = "input/day02.txt";
    let contents = read_file(file_path);
    
    let mut part1_answer: i64 = 0;
    let mut part2_answer: i64 = 0;

    for range in contents.split(",") {
        let parts: Vec<&str> = range.split("-").collect();

        if parts.len() == 2 {
            let (start, end) = (parts[0], parts[1]);
            let start: i64 = start.parse().unwrap();
            let end: i64 = end.parse().unwrap();
            
            for num in start..(end + 1) {
                if is_repeating_twice(num.to_string()) {
                    part1_answer += num;
                }

                if is_repeating(num.to_string()) {
                    part2_answer += num;
                }
            }
        } else {
            println!("Parts is not of length 2")
        }
    }

    println!("Part 1 Answer: {part1_answer}");
    println!("Part 2 Answer: {part2_answer}");
}

fn is_repeating_twice(num: String) -> bool {
    let num_length = num.len();

    if num_length == 0 || num_length % 2 != 0{
        return false;
    }

    let half_index = num_length / 2;
    let substring = &num[0..half_index];
    let fullstring = substring.repeat(2);

    if fullstring == num {
        // yay we found it
        return true;
    }

    return false;
}

fn is_repeating(num: String) -> bool {
    let num_length = num.len();

    if num_length == 0 {
        return false;
    }

    for substring_length in 1..(num_length / 2 + 1) {
        if num_length % substring_length != 0 {
            continue;
        }
        let substring = &num[0..substring_length];
        let fullstring = substring.repeat(num_length / substring_length);
        if fullstring == num {
            // yay we found it
            return true;
        }
    }
    return false;
}