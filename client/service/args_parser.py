import argparse

parser = argparse.ArgumentParser(description='Test the performance of main verifications in Election Transparency')
# parser.add_argument('--logserver_url', help='Address and port of the log server', nargs='?', default="localhost:8000", type=str)
parser.add_argument('--sample_size', help='Number of repetition for each operation', nargs='?', default=50, type=int)