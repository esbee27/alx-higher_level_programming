#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0

    arg_len = len(sys.argv)
    for i in range(1, arg_len):
        result += int(sys.argv[i])
    print(f"{result}")
