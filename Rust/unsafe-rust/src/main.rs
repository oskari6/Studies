use std::ptr;

enum Win2 { //union type
    Bronze(i32),
    Silver(i32),
    Gold(i32),
}
union Win { //union type
    Bronze: i32,
    Silver: i32,
    Gold: i32,
}
static mut POINTS : i32 = 10;//mut has to surrounded unsafe

unsafe trait Test_trait {
    unsafe fn test2();
}

unsafe impl Test_trait for i32 {
    unsafe fn test2(){
        let a = 10;
        let ptr : *const i32 = &a;
        let b = Box::new(10); //smart pointer
        let ptr2: *const i32 = &*b; //smart pointer
    
        let ptr3: *const i32 = ptr::null(); //null pointer, never dereference
    
        println!("The value is {}", *ptr);
    
        //derefereshing a pointer, other way to use unsafe
        // unsafe {
        //     println!("The value is {}", *ptr);
        // }
    }
}
//unsafe function
unsafe fn test(){
    let a = 10;
    let ptr : *const i32 = &a;
    let b = Box::new(10); //smart pointer
    let ptr2: *const i32 = &*b; //smart pointer

    let ptr3: *const i32 = ptr::null(); //null pointer, never dereference

    println!("The value is {}", *ptr);

    //derefereshing a pointer, other way to use unsafe
    // unsafe {
    //     println!("The value is {}", *ptr);
    // }
}

fn main() {
    // unsafe {
    //     test();
    // }
    // unsafe {
    //     println!("{POINTS}");
    // }

    // unsafe {
    //     i32::test2();
    // }

    // let win = Win {Silver: 30};
    // unsafe {
    //     println!("{}", win.Silver);
    // }

    let win = Win2::Silver(30);

    if let Win2::Silver(val) = win {
    println!("{}", val);
}
}
