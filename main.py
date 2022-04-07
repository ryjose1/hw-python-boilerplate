from config import Config
import argparse
import helloworld


def main():
    cf = Config()

    parser = argparse.ArgumentParser()
    parser.add_argument("operation", type=str, help="the operation to run")
    args = parser.parse_args()

    print("Operation ", args.operation)
    cf.newConfig("bar")

    helloworld.hmm()

if __name__ == "__main__":
    main()