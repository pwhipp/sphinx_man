

def verify_signatures(repo, old_commit, new_commit, changes):
    changes = add_signature_requirements(repo, old_commit, changes)
    changes = add_signatures(repo, new_commit, changes)


def add_signature_requirements(repo, old_commit, changes):
    return changes


def add_signatures(repo, new_commit, changes):
    return changes
