OUT:=target
CFG:=debug
BIN:=idlx
SRC:=rs
EXT:=rs

SRCFILE:=$(SRC)/$(BIN).$(EXT)
BINFILE:=$(OUT)/$(CFG)/$(BIN)

default: setup build run

setup:
	@echo "setup"

build:
	cargo build --package ix-lsp 

run:
	./$(BINFILE)
	
%.rs:
	cargo build --package ix-lsp --release
	cargo run

install:
	cargo install --package ix-lsp .

