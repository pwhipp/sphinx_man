import os
from src.exceptions import RepositoryExistsError

# todo: get create to create a repository
# todo: add governor hook and get arbitrary accept/reject
# todo: ffonly, main branch only
# todo: add githook, passing data to python function which rejects push with reason as appropriate
#

god_example = {'lastname': 'Bloggs',
               'firstname': 'Joseph',
               'username': 'jo',
               'public_key': "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKyvWsPSQ/7N0dpJBMCWeQ0Jp/fgLOsEpOz/gn8tIPJx paul@PWC1"}


def create(path=None, god=None):
    """Create a new bare protected_repository at path with any essential initial structure and content.
    Protect it with a git hook on push to enforce the signature rules."""
    if path is None:
        path = os.getcwd()
    if god is None or getattr(god, 'public_key', None) is None:
        raise Exception("god must be supplied and must have a valid public key")

    if not os.path.isdir(path):
        os.makedirs(path)

    if os.path.isdir(os.path.join(path, '.git')):
        raise RepositoryExistsError(f"{path} already contains a .git directory!")

    # Add god and initial signing rule
    # Commit
    # Add governor hook
    pass


def clone(protected_repository, path=None, prevent_invalid_pushes=True):
    """Create a working protected_repository at path"""
    if prevent_invalid_pushes:
        # Use a template (from protected_repository?) to ensure all necessary hooks are in place to check and reject push
        # attempts that are not properly signed
        template = 'A'
    else:
        template = 'B'

    pass


def governor_hook(push_info, signatures):
    """
    Use push_info to generate signature_requirement using repo signing rules.
    verify sign
    """
    signature_requirement = get_signature_requirement(push_info)
    if verify_signatures(signature_requirement, signatures):
        pass  # do push
    pass  # reject push
