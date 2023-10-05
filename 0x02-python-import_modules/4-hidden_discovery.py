#!/usr/bin/python3
# a program that prints all the names defined by the compiled module hidden
if __name__ == "__main__":
    import hidden_4
    all_names_ = dir(hidden_4)
    for eachname in all_names_:
        if eachname[:2] != "__":
            print(eachname)
