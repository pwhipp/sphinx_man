Signing Rules
=============

A .signing_rules.yaml file may be placed in any project folder.
The content of the .signing_rules affects patches relating to the folder's files and folders recursively.

The patches consist of a set of effects each of which generates a .signing_rules using the hierarchy. These .signing_rules
are then combined into a single file using the merge_effect_signing_rules function which combines the numeric parameters to take the 'most restrictive' option. Mismatches of other parameters generate an error and prevent consideration of the patch (two patches might be needed in the unlikely event of this occurring).

The .signing_rules.yaml file is a part of the project and may be patched like any other file.

Signing rules may govern pattern specific determination of:

- The minimum allowable deadline in terms of time plus patch submission time
- The deadline for the decision to be made (must be >= minimum above)
- The signing criteria required to accept or reject a patch
- Merging criteria for the signing_rules

Signing
-------

We have a 'main' branch which is the consensually correct content.

A vote is a signature so in e.g. people, someone who has the role 'ipsc_instructor' can give someone the role of 'ipsc_competitor' by signing a

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

From the perspective of signing, the issue must consist of a diff and the commit to which it applies. If the diff cannot be cleanly applied, the issue should be rejected as a signing issue (we're aiming for clarity and automation).

For the purposes of signing rules, we only consider folders because all file changes are viewed as a change to the folder
containing the files. Thus signing rules are only concerned with:

- added folders == changed (parent) folder
- deleted folders == changed (parent) folder
- changed folder == changed (parent) folder

We call these the issue's effect which is thus a list of the changed folders.

In order to fully identify an issue, we need the starting state and the proposed changes to that state.

If an issue (patch) changes... What does changing it mean. It is really just a new patch but it will often based on some other patch. This progresses through folder changes e.g.

requested_patches/<shared_path>/<patch name>/[<patch>,<reason_needed>,<synopsis>,['new','simplification', 'enhancement', 'clarification']

Anyone can create.

signing rule to accept and move to proposed_patches/....

Users
~~~~~
A user is identified to the system as the private key owner of a public key. Challenge/response may be used to verify

Signing
~~~~~~~

up_vote(issue)
down_vote(issue)

An up_vote or down_vote is a modified signature on the patch.

Delegation
----------

Tom wants to delegate all finance and signing policy issues to Alice:

create_delegation_request(/finance, alice) -> creates request
accept_delegation_request(request) -> sends acceptance and means alice's votes on finance issues now count for Tom too
cancel_delegation_request(request) - this can be done by the delegator or the delegatee

delegation_request is an object specifying delegated re patterns e.g.
    - .signing_rules
    - /finance

and the proposed delegate, signed by the delegator.

It becomes a delegation when signed by the delegatee.

signing/signers
signing/delegations

Maybe delegate up_votes (vote up if delegatee up_votes), down_votes or both_votes.

Sticky Signing
-------------

If a signer applies a sticky vote then it will be automatically recast if the issue is resubmitted with changes rather than needing to vote again. This would usually mean just minor amendments to detail so is handy in practice if the signer trusts the authors



Signing Privacy
--------------

Votes are private unless they are delegatee votes in which case the delegatee is named with a count (the delegator is not shown)



Voters
------

A signer is defined as an annotated public key in the signers folder. Adding a signer requires signing just like anything else.

- Anyone verified
     have rules in the signers folder requiring
       - a vote solely from the author (automatic)
       - key verification/validation from some service
       - No other file in the folder with a vote from this author


Breaking the system
-------------------

It will always be possible to create a set of signing rules that prevent any further signing or overly de-restrict things leading to meaningless content. 'Signing templates' may be used to create hierarchies with a 'veto' role allowing prevention of adoption, a 'unilateral' role allowing users with that role to 'just do it' etc.

Accommodating changes
---------------------

When an issue is accepted, all subsequent issues logically change (because the starting state is no longer the same)

Relevant Voters
---------------

The system here allows signers to delegate which is cool but delegating is not enough to deal with 'irrelevance'. If using patchvote for local government for example then residents of Samford will see a local by-pass as highly relevant and will want to vote on it. Nobody living more than a few miles from the affected area is likely to  care much (apart from possibly wanting the by-pass for convenient travel).

Delegation could cover this in practise by including negated matching:
  /main_roads.*
  !/main_roads/locale/Samford.*

Roles
-----

A role is a string assigned to a signer by patch in the normal way.

.. code-block:: yaml

    name: (unique key)
    unique: boolean
    description:
    required_support: 0.51
    effect:
      auto_delegation:
        '/.*'
        '!/finance'

Roles are allocated by vote (signature) according to the role specification. For unique roles, a vote by a user can only go to one candidate. If this
happens,

Certification
-------------

An RO must pass something - signer must have a declaration signed by an appropriate trainer

So we do need roles (which are voted to users) and certification is then a signed pairing of a certificate and a signer by a 'certifier'

hmm...

person -> prospect (certified by 'new_member_officer' - user and officer must sign certificate)
prospect -> member (===signer) ditto
member -> officer (certified by someone appropriate)

roles may expire. signer is a role.

candidacy
candidate <president>
requires membership certificate >= n years old
requires 10 member votes

certificates/candidacy/roles are contracts!
A contract has some certifier role...

TheBook pages are contracts? TheBook is a contract? patches are agreed contract changes.


So we have a mongodb database.
It has a collection of people

operations
create_proposal(proposal, authors, signatures)
update_proposal(proposal, authors, signatures) -> resets clock, notifies & deletes invalidated signatures
execute_proposal(proposal) -> pass/fail time not expired, insufficient signatures, success -> changes database.
sign_proposal(proposal, person)


notifications -
signature_invalidated (sign again?)
proposal_accepted
proposal_rejected