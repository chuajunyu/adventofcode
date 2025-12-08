use aoc2025::read_file;

fn main() {
    let file_path = "input/day03.txt";
    let contents = read_file(file_path);

    let mut part1_answer = 0;
    let mut part2_answer = 0;

    for mut line in contents.split("\n") {
        if line.strip_suffix("\r") != None {
            line = line.strip_suffix("\r").unwrap();
        }

        part1_answer += find_joltage(line.to_string(), 2);
        part2_answer += find_joltage(line.to_string(), 12);
    }

    println!("Part 1 Answer {part1_answer}");
    println!("Part 2 Answer {part2_answer}");
}


fn find_joltage(line: String, battery_limit: i32) -> i64 {
    let line_length = line.len();

    let mut joltage: i64 = 0;
    let mut joltage_vec: Vec<i32> = vec![0; battery_limit as usize];

    // loop through each character
    for (index, char) in line.chars().enumerate() {

        // convert each character to an integer
        let num: i32;
        if char.to_digit(10) != None {
            num = char.to_digit(10).unwrap() as i32;
        } else {
            println!(" num is uninitialized");
            return 0;
        }

        // LHS gives what number it is from the back
        if line_length - index > battery_limit as usize {
            for index in 0..joltage_vec.len() {
                if num > joltage_vec[index] {
                    joltage_vec[index] = num;

                    // set the rest of the joltage vec to be 0
                    let rest_of_vec = &mut joltage_vec[index + 1..];
                    rest_of_vec.fill(0);
                    break;
                }
            }
        } else {
            // we can only compare with the same index from now on
            let joltage_index = battery_limit as usize - (line_length - index);
            
            for j in joltage_index..battery_limit as usize {
                // println!("{j}, {num} > {:?}", joltage_vec[j]);
                if num > joltage_vec[j] {
                    
                    joltage_vec[j] = num;

                    // set the rest of the joltage vec to be 0
                    let rest_of_vec = &mut joltage_vec[j + 1..];
                    rest_of_vec.fill(0);
                    break;
                }
            }

        }
        
    }
    
    for &n in &joltage_vec {
        joltage *= 10;
        joltage += n as i64;
    }

    println!("{:?}", joltage_vec);

    return joltage;

}