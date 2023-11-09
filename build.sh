rm -rf target
cargo build --release
strip -o bin/cpc_arm target/release/CAIE_Code
# strip -o bin/cpc_x86 target/release/CAIE_Code
