use std::mem; //swapping

fn swap(first: &mut String, last: &mut String) {
    mem::swap(first, last);
}

fn greet(first:String, last:String)-> (String, String){
    println!("hello {first} {last}");
    (first, last)
}

fn greet2(first:&str, last:&str){//"string" can be passed in now not just variable
    println!("hello {first} {last}");
}

//create data in a function
fn generate_name() -> (String, String) {
    let third = String::from("third");
    let fourth = String::from("fourth");
    (third, fourth)
}
fn main() {
    let mut first = String::from("first");
    let mut last = String::from("last");
    (first, last) = greet(first, last);
    println!("{first} {last}"); //without mut this is not possible due to carbage collector
   
   let (mut third, mut fourth) = generate_name();
   println!("{third}{fourth}");

   greet2(&first, &last);

   swap(&mut first, &mut last);
   greet2(&first, &last);

   let name2 = String::from("name");
   let last2 = String::from("name2");

   greet2(name2.as_str(), last2.as_str());
   
   // let n: &String;
    // {
    //     let name = String::from("name");
    //     n = &name;  //reference
    //     println!("{n}");
    // }

    //this doesnt work because of ownership change. (not the case for primitives)
    // let first = String::from("name");
    // let name = first;
    // println!("{first}");

    //clone
    // let name = String::from("first");
    // let name2 = name.clone();

    // println!("{name} {name2}");

    //reference
    // let name = String::from("first");
    // let name2 = &name;
    // let name3 = &name;

    // println!("{name} {name2} {name3}");

    //mutable reference
    // let mut name = String::from("first");
    // let name2 = &mut name;
    // *name2 = String::from("second");
    // println!("{name2}");
}
