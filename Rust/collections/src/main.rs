use num_derive::{FromPrimitive, ToPrimitive};
use num_traits::FromPrimitive;
use std::{collections::HashMap, fmt, io};

#[derive(Debug, FromPrimitive, ToPrimitive, Eq, PartialEq, Hash)] //:?, displays the default values of Gem
enum Gem {
    Diamond = 1,
    Sapphire,
    Ruby,
    Topaz,
    Onyx,
    Jade,
}

//instead of from_u8()
/*impl Gem {
    fn from_number(num: u8) -> Option<Gem>{
        match num {
            1 => Some(Gem::Diamond),
            2 => Some(Gem::Sapphire),
            3 => Some(Gem::Ruby),
            4 => Some(Gem::Topaz),
            5 => Some(Gem::Onyx),
            6 => Some(Gem::Jade),
            _ => None,
        }
    }
}*/

//Display trait, for custom formatting
impl fmt::Display for Gem {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            Gem::Diamond => write!(f, "Diamond"),
            Gem::Sapphire => write!(f, "Sapphire"),
            Gem::Ruby => write!(f, "Ruby"),
            Gem::Topaz => write!(f, "Topaz"),
            Gem::Onyx => write!(f, "Onyx"),
            Gem::Jade => write!(f, "Jade"),
        }
    }
}

fn game(map: &mut [[u8; 5]; 5]) -> Vec<Gem> {
    let mut found: Vec<Gem> = Vec::new();

    while found.len() < 5 {
        println!("Search an X Y position (example input: 4 3): ");
        let mut input = String::new();

        match io::stdin().read_line(&mut input) {
            Ok(_) => {}
            Err(_) => {
                println!("Failed to read line");
                continue;
            }
        }

        let parts: Vec<&str> = input.trim().split_whitespace().collect();

        if parts.len() != 2 {
            println!("Two numbers required");
            continue;
        }

        let (x, y) = match (parts[0].parse::<u8>(), parts[1].parse::<u8>()) {
            (Ok(x), Ok(y)) => (x, y),
            _ => {
                println! {"Something wrong with the input"};
                continue;
            }
        };

        if x >= 5 || y >= 5 {
            println!("Invalid index");
            continue;
        }

        let data = map[x as usize][y as usize];

        let gem = match Gem::from_u8(data) {
            Some(gem) => gem,
            None => {
                println!("No gem foun at that position");
                continue;
            }
        };
        found.push(gem);
        map[x as usize][y as usize] = 0;
        println!("{found:?}");
    }
    found
}
fn main() {
    // let gem1 = (Gem::Onyx, 25.00);
    // let gem2 = (Gem::Jade, 10.00);//_f32 to change type
    // let gem3 = (Gem::Jade, 15.00, 10);//tuples ()

    let gems = [
        (Gem::Onyx, 25.00),
        (Gem::Diamond, 100.00),
        (Gem::Onyx, 50.00),
        (Gem::Ruby, 10.00),
    ]; //array, same type

    for gem in gems {
        println!("This {} is worth {}", gem.0, gem.1); //.1 or .0 second element of tuple
    }

    let mut map = [[0; 5]; 5]; //filled with false, 2d array
    map[4][2] = 1;
    map[1][2] = 2;
    map[3][3] = 3;
    map[0][2] = 4;
    map[1][4] = 5;

    let mut found: Vec<Gem> = game(&mut map);

    println!("Congrats, you found all of the gems!");

    //hashmaps
    let mut gem_values: HashMap<Gem, f64> = HashMap::new();
    gem_values.insert(Gem::Diamond, 1000.00);
    gem_values.insert(Gem::Jade, 9000.00);
    gem_values.insert(Gem::Onyx, 8000.00);
    gem_values.insert(Gem::Topaz, 7000.00);
    gem_values.insert(Gem::Ruby, 6000.00);
    gem_values.insert(Gem::Sapphire, 5000.00);

    let mut sum = 0.0;
    for gem in found {
        sum += gem_values[&gem];
    }

    println!("Values of gems: {}", sum)
}
