cargo build --release
remove-item bin/cpc.exe
move-item -path target/release/CAIE_Code.exe -destination bin/cpc.exe
