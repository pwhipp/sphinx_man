"""
Assumes a bare repository
"""
import os
import sys
import logging
from collections import defaultdict

from git import Repo

from protrep.settings import LOGGING
from protrep.verify_signatures import verify_signatures


logging.basicConfig(**LOGGING)


def pre_receive():
    logging.debug("pre_receive: entered")
    update_map = read_update_map(sys.stdin)
    for ref in update_map:
        logging.debug(f"pre_receive: ref change: {ref} {update_map[ref]['old']} {update_map[ref]['new']}")

    master_update = update_map.get('refs/heads/master', None)
    if master_update is None:
        logging.debug("pre-receive: No master reference update. Skipping processing for now")
        return

    repo = Repo.init(os.getcwd(), bare=True)

    old, new = [repo.commit(master_update[which]) for which in ['old', 'new']]
    changes_text = repo.git.diff('--name-status', f'{old}..{new}')
    changes = get_change_summary(changes_text)
    verify_signatures(repo, old, new, changes)


def read_update_map(f):
    return {ref: {'old': old, 'new': new}
            for old, new, ref in [line.split() for line in f]}


def get_change_summary(git_diff_status_text):
    """Return dict with lists of files 'A'dded, 'M'odified or 'D'eleted."""

    changes_lines = [line.split() for line in git_diff_status_text.split('\n')]
    changes = defaultdict(list)
    for line in changes_lines:
        changes[line[0]].append(line[1])
    return dict(changes)


if __name__ == "__main__":
    pre_receive()
