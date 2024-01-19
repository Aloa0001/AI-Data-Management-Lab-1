import sys
import requests

from datetime import datetime


def send(name, web=None):
    r = requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        return "There was an error!"


if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    print(send("a", "b"))
    print("Name: ", name)


def test():
    print("test")
