if ! type tty-share >/dev/null 2>&1; then
	brew install tty-share
fi

tty-share -L 7788 -A
