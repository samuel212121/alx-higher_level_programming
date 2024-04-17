#!/usr/bin/python3
def read_file(filename=""):
    filename = "UTF8.txt"
    with open('UTF8.txt', 'r', encoding="utf-8") as f:
        read_file = f.read()
