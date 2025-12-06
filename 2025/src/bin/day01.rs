use aoc2025::read_file;

fn main() {

    // write a function to read the day1.txt file

    let file_path = "input/day01.txt";
    let contents = read_file(file_path);

    // initialise a counter variable and a dial variable
    let mut part1_answer = 0;
    let mut part2_answer = 0;
    let mut counter = 0;
    let mut dial = 50;
    let mut end = false;

    // Loop through each line and apply changes, remember overflow logic
    loop {

        // extract the current line
        let mut dir = None;
        let mut mag = String::new();
        loop {
            if let Some(char) = contents.chars().nth(counter) {
                
                if char == '\r' {
                    counter += 1;
                    continue;
                }
                if char == '\n' {
                    counter += 1;
                    break;
                }

                if dir == None {
                    dir = Some(char);
                } else {
                    mag.push(char);
                }
                counter += 1;
            } else {
                println!("No character found at index {}", counter);
                end = true;
                break;
            }
        }   


        let mut magnitude: i32 = mag.parse().unwrap();
        if let Some(direction) = dir {
            // normalise the magnitude first
            loop {
                if magnitude >= 100 {
                    magnitude -= 100;
                    part2_answer += 1;
                    // println!("added 1 norm");
                } else {
                    break;
                }
            }

            // case 1, positive to positive
            // case 2, 0 to negative
            // case 3, 0 to positive
            // case 4, positive to negative
            // case 5, positive to >=100

            let prev_dial = dial;

            if direction == 'L' {
                dial -= magnitude;
            } else if direction == 'R' {
                dial += magnitude;
            }

            if 0 <= dial && dial <= 99 {
                if dial == 0 && ! (prev_dial == 0) {
                    part2_answer += 1;
                    // println!("added 1 case 6");
                }
            } else {
                if dial < 0 {
                    dial += 100;
                    if prev_dial != 0 {
                        part2_answer += 1;
                        // println!("added 1 case 4");
                    }
                }

                if dial > 99 {
                    // println!("added 1 case 5");
                    dial -= 100;
                    part2_answer += 1;
                }
            
            }

            if dial == 0 {
                part1_answer += 1
            }
        }

        if end {
            println!("Part 1 Answer: {part1_answer}");
            println!("Part 2 Answer: {part2_answer}");
            break;
        }
    }
}

    

    



