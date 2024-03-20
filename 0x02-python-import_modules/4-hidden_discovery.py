#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    str = dir()
    for i in range(0, len(str)):
        if str[i][0:2] != "__":
            print("{}".format(str[i]))
