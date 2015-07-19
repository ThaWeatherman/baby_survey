import argparse

from app import app


parser = argparse.ArgumentParser()
parser.add_argument('-d', action='store_true', help='Run this application in debug mode')
parser.add_argument('-p', type=int, default=8000, help='The port to run this on')
parser.add_argument('-H', type=str, default='127.0.0.1', help='The interface to run this application on')
args = parser.parse_args()

app.run(host=args.H, port=args.p, debug=args.d)
