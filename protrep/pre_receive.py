import sys
import logging

from protrep.settings import LOGGING

logging.basicConfig(**LOGGING)


def post_receive():
    update_map = read_update_map(sys.stdin)
    for ref in update_map:
        logging.debug(f"post_receive: {ref} {update_map[ref]['old']} {update_map[ref]['new']}")


def read_update_map(f):
    return {ref: {'old': old, 'new': new}
            for old, new, ref in [line.split() for line in f]}


if __name__ == "__main__":
    post_receive()
