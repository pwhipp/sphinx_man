Voting Rules
============

Maybe make this a mongodb thing. The patchrules application will apply or reject patches.
Make it sit alongside a repo? Make Mongo the repo??

If I make mongodb the repo then I'll need to be able to publish the canonical document and, with patches, publish the 'diff' version in a nice way - not just the new version, a sphinx document that shows added/removed/changed sections.

A .voting_rules.yaml file may be placed in any project folder.
The content of the .voting_rules affects patches relating to the folder's files and folders recursively.

The patches consist of a set of effects each of which generates a .voting_rules using the hierarchy. These .voting_rules
are then combined into a single file using the merge_effect_voting_rules function which combines the numeric parameters to take the 'most restrictive' option. Mismatches of other parameters generate an error and prevent consideration of the patch (two patches might be needed in the unlikely event of this occurring).

The .voting_rules.yaml file is a part of the project and may be patched like any other file.

Voting rules may govern pattern specific determination of:

- The minimum allowable deadline in terms of time plus patch submission time
- The deadline for the decision to be made (must be >= minimum above)
- The voting criteria required to accept or reject a patch
- Merging criteria for the voting_rules

Voting
------

We have a 'main' branch which is the consensually correct content.

Issues
~~~~~~

An issue is a particular change to a tree of folders and files such as:

::

    great_apes
    ├── african_apes
    │   ├── chimpanzees
    │   ├── gorillas
    │   │   ├── eastern_gorilla.yaml
    │   │   ├── info.yaml
    │   │   └── western_gorilla.yaml
    │   ├── human.yaml
    │   └── info.yaml
    ├── info.yaml
    └── orangutans
        ├── bornean_orangutan.yaml
        ├── info.yaml
        └── sumatran_orangutan.yaml

The issue consists of one or more

- added files
- changed files
- deleted files
- added folders
- deleted folders

From the perspective of voting, the issue must consist of a diff and the commit to which it applies. If the diff cannot be cleanly applied, the issue should be rejected as a voting issue (we're aiming for clarity and automation).

For the purposes of voting rules, we only consider folders because all file changes are viewed as a change to the folder
containing the files. Thus voting rules are only concerned with:

- added folders == changed (parent) folder
- deleted folders == changed (parent) folder
- changed folder == changed (parent) folder

We call these the issue's effect which is thus a list of the changed folders.

In order to fully identify an issue, we need the starting state and the proposed changes to that state.

If an issue (patch) changes... What does changing it mean. It is really just a new patch but it will often based on some other patch. This progresses through folder changes e.g.

requested_patches/<shared_path>/<patch name>/[<patch>,<reason_needed>,<synopsis>,['new','simplification', 'enhancement', 'clarification']

Anyone can create.

voting rule to accept and move to proposed_patches/....

Users
~~~~~
A user is identified to the system as the private key owner of a public key. Challenge/response may be used to verify

Voting
~~~~~~

up_vote(issue)
down_vote(issue)

An up_vote or down_vote is a modified signature on the patch.

Delegation
----------

Tom wants to delegate all finance and voting policy issues to Alice:

create_delegation_request(/finance, alice) -> creates request
accept_delegation_request(request) -> sends acceptance and means alice's votes on finance issues now count for Tom too
cancel_delegation_request(request) - this can be done by the delegator or the delegatee

delegation_request is an object specifying delegated re patterns e.g.
    - .voting_rules
    - /finance

and the proposed delegate, signed by the delegator.

It becomes a delegation when signed by the delegatee.

voting/voters
voting/delegations

Maybe delegate up_votes (vote up if delegatee up_votes), down_votes or both_votes.

Sticky Voting
-------------

If a voter applies a sticky vote then it will be automatically recast if the issue is resubmitted with changes rather than needing to vote again. This would usually mean just minor amendments to detail so is handy in practice if the voter trusts the authors



Voting Privacy
--------------

Votes are private unless they are delegatee votes in which case the delegatee is named with a count (the delegator is not shown)



Voters
------

A voter is defined as an annotated public key in the voters folder. Adding a voter requires voting just like anything else.

- Anyone verified
     have rules in the voters folder requiring
       - a vote solely from the author (automatic)
       - key verification/validation from some service
       - No other file in the folder with a vote from this author


Breaking the system
-------------------

It will always be possible to create a set of voting rules that prevent any further voting or overly de-restrict things leading to meaningless content. 'Voting templates' may be used to create hierarchies with a 'veto' role allowing prevention of adoption, a 'unilateral' role allowing users with that role to 'just do it' etc.

Accommodating changes
---------------------

When an issue is accepted, all subsequent issues logically change (because the starting state is no longer the same)

Blame
-----