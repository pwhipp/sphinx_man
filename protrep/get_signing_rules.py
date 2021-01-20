import os
import yaml

from protrep.settings import SIGNING_RULES_FILENAME


def get_signing_rules(path):
    signing_rule_files = get_signing_rule_files(path)
    signing_rule_sets = [rule_set for f in signing_rule_files if (rule_set := _load_signing_rule_file(f))]
    if not signing_rule_sets:
        return {}
    signing_rules = signing_rule_sets[0]
    for additional_rule_set in signing_rule_sets[1:]:
        signing_rules = merge_signing_rules(signing_rules, additional_rule_set)
    return signing_rules


def get_signing_rule_files(path):
    possible_rule_files = [rule_file for d in DirsAbove()(path)
                           if os.path.isfile(rule_file := os.path.join(d, SIGNING_RULES_FILENAME))]
    return possible_rule_files


class DirsAbove:

    def __init__(self):
        self.dir_root = ''

    def __call__(self, path):
        self.dir_root = ''
        return [self.full_folder(folder) for folder in os.path.dirname(path).split('/')]

    def full_folder(self, folder):
        self.dir_root = os.path.join(self.dir_root, folder)
        return self.dir_root


def _load_signing_rule_file(rule_file):
    with open(rule_file, 'r') as f:
        return yaml.load(f, yaml.SafeLoader)


def merge_signing_rules(a, b):
    return mapping_merge(a, b)


def mapping_merge(a, b):
    """Arbitrary mapping where values that are dicts are combined with values in b taking precedence"""
    result = {**a}
    for bk in b:
        if bk in result and isinstance(result[bk], dict) and isinstance(b[bk], dict):
            result[bk] = mapping_merge(result[bk], b[bk])
            continue
        result[bk] = b[bk]
    return result
