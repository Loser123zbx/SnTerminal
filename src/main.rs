use std::fs;
use std::path::Path;

fn main() {
    let file_path = "src/version.json";
    
    if Path::new(file_path).exists() {
        let content = fs::read_to_string(file_path).unwrap();
        println!("{:?}", content);
    } else {
        eprintln!("文件 {} 不存在", file_path);
    }
}
