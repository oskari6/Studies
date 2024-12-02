use rand::Rng;
use std::{cmp::Ordering, io};

fn main() {
    println!("How many numbers to guess?: ");
    let mut how_many = String::new();
    io::stdin()
        .read_line(&mut how_many)
        .expect("Error reading input");

    let num_guesses: u8 = how_many.trim().parse().expect("Error readin input");

    let mut correct = Vec::new(); //vector

    //for loop
    for _ in 0..num_guesses {
        correct.push(rand::thread_rng().gen_range(1..=10));
    }

    //println!("{correct:?}");
    // let mut first = "first";
    // let mut second = "second";
    //let data = [1, 2, 3, 4];

    //println!("Hello, world {first} {}!", second.to_lowercase()); //methods after ,
    //println!("{data:?}") //debug format :?

    //let correct = rand::thread_rng().gen_range(1..=10);
    //println!("correct: {correct}");

    let mut guesses_made = 0;
    println!("Guess a number: ");

    //while loop, normal loop = loop {}
    while guesses_made < num_guesses {
        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Error reading input");

        //new variables with same name can be created

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(e) => {
                println!("Error with parse, try again");
                continue;
            }
        };

        //if expression allows to return values
        // let mut message = if correct < guess {
        //     String::from("Too high!")
        // } else if correct > guess {
        //     String::from("Too low!")
        // } else {
        //     String::from("Correct!")
        // };

        //match
        match guess.cmp(&correct[guesses_made as usize]) {
            //index needs to be cast as usize when used like this
            Ordering::Greater => println!("Too high!"),
            Ordering::Less => println!("Too low!"),
            Ordering::Equal => {
                println!("Correct!");
                guesses_made += 1;
                if guesses_made < num_guesses {
                    println!("Next number!");
                }
            }
        };
    }
    println!("Thanks for playing, correct answers below: ");
    for item in correct {
        println!("{item}");
    }
    //println!("You guessed {}, Welcome", guess.trim()); //trim because \n
}
