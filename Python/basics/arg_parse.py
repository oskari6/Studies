import argparse

parser = argparse.ArgumentParser(description="test parser")

parser.add_argument("--name", type=str, help="your name")
parser.add_argument("--age", type=int, help="Your age")
parser.add_argument("--verbose", action="store_true", help="increase output verbosity")

args = parser.parse_args()

#access
# args.name
# args.age
# args.verbose

# command to run
# python arg_parse.py --name "Alice" --age 30 --verbose

#json
parser.add_argument("--config", type=argparse.FIleType("r"), help="configuration file")