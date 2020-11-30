Voting Rules
============

A .voting_rules.yaml file may be placed in any project folder.
The content of the .voting_rules affects patches relating to the folder's files and folders recursively.

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

Voters
------

A voter is defined as an annotated public key in the voters folder. Adding a voter requires voting just like anything else.

- Anyone verified
     have rules in the voters folder requiring
       - a vote solely from the author (automatic)
       - key verification/validation from some service
       - No other file in the folder with a vote from this author

Collaboration
-------------

Say Douglas has everyone's /finance delegation so he becomes 'Chief of Finance' and Mary has everyone's '/military' delegation so she becomes 'Chief of Military'. If Douglas and Mary collaborate and submit an issue that allocates an additional 10% of the total budget to the military. If this only changes
content under /finance and under /military none of their delegated votes would count intuitively (they are precluded by the opposing folder content change). OTOH if each creates an issue under their own folder that 'happens' to match. Each can automatically accept the issue, even though it is really one issue.

One resolution of this story is to distribute stuff (e.g a finance allocation is a minus under some location and a plus elsewhere) but that quickly becomes artificial.

We don't want Mary and Douglas to collaborate with separate issues - we want them to create a single issue. Therefore we need to merge the delegators across our delegatees with some algorithm such that it is easier for Mary and Douglas to do the 'right thing':

The issue affects [/finance, /military]. The vote collection goes something like:

.. code-block:: python

   turnout = 0
   votes = 0
   for voter in voters:
        if voter_has_signed:
            turnout += 1
            votes = votes + up_or_down(signature)
        else:  # allow for multiple delegate involvement
            delegated_vote_made = False
            delegated_vote = 0
            for effect in issue_effects:
                for delegatee in delegatees(voter, effect):
                    if delegatee_has_voted:
                        delegated_vote_made = True
                        delegated_vote += delegatee_vote
                    else:  # all applicable delegatees must have voted
                        delegated_vote_made = False
                        break
            if delegated_vote_made:
                turnout += 1
                votes = votes + delegated_vote

Breaking the system
-------------------

It will always be possible to create a set of voting rules that prevent any further voting or overly de-restrict things leading to meaningless content. 'Voting templates' may be used to create hierarchies with a 'veto' role allowing prevention of adoption, a 'unilateral' role allowing users with that role to 'just do it' etc.