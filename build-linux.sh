cargo build --release
mkdir bin/linux
mkdir bin/linux/kali
mkdir bin/linux/kali/arm64
mv target/release/CAIE_Code bin/linux/kali/arm64/cpc
