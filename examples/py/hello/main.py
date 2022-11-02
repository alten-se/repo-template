from hello.math import add_two

derp = "very long str asdaslkdjasldjaslkjdalksjdlkajsdlkasjdlaksjdlaksjdlaksjdalsjkdalskdjalskdjalskdj"


def hello(              ):
    print("Hello, world!")


def run():
    hello()
    five = add_two(3)
    print(f"what comes after four is: {five}")


if __name__ == "__main__":
    run()
