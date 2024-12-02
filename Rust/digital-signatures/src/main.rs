use bls_signatures::PrivateKey;
use rand::thread_rng;
use serde::{Deserialize, Serialize};

#[derive(Deserialize, Serialize)]

struct Transaction {
    from: String,
    to: String,
    amount: i128
}

fn main() {
    let private = PrivateKey::generate(&mut thread_rng());
    //let private2 = PrivateKey::generate(&mut thread_rng()); //wont work with this

    let public = private.public_key();

    // println!("{private:?}");
    // println!("{public:?}");

    //let message = "Message sample";

    let message = Transaction {
        amount: 100,
        from: String::from("User"),
        to: String::from("User2"),
    };

    let serialized_message = serde_json::to_string(&message).unwrap();

    //let sig = private.sign(message);

    let sig = private.sign(&serialized_message);

    //let verification = public.verify(sig, message);
    let verification = public.verify(sig, &serialized_message);

    println!("Is the message authentic? {}", verification);

    let deserialized_message : Transaction = serde_json::from_str(&serialized_message).unwrap();

    println!("Amount: {}", deserialized_message.amount);
}
