#!/bin/sh

if ! xcode-select -p &> /dev/null; then
	xcode-select --install
    exit 33
else
    exit 0
fi