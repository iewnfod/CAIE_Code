rm -rf target
cargo build --release
strip -o bin/cpc target/release/CAIE_Code
