Collaboration
=============

Say Douglas has everyone's /finance delegation so he becomes 'Chief of Finance' and Mary has everyone's '/military' delegation so she becomes 'Chief of Military'. If Douglas and Mary collaborate and submit an issue that allocates an additional 10% of the total budget to the military. If this only changes
content under /finance and under /military none of their delegated votes would count intuitively (they are precluded by the opposing folder content change). OTOH if each creates an issue under their own folder that 'happens' to match. Each can automatically accept the issue, even though it is really one issue.

One resolution of this story is to distribute stuff (e.g a finance allocation is a minus under some location and a plus elsewhere) but that quickly becomes artificial.

We don't want Mary and Douglas to collaborate with separate issues - we want them to create a single issue. Therefore we need to merge the delegators across our delegatees with some algorithm such that it is easier for Mary and Douglas to do the 'right thing':

The issue affects [/finance, /military]. The vote collection goes something like:

.. code-block:: python

   turnout = 0
   votes = 0
   for signer in signers:
        if signer_has_signed:
            turnout += 1
            votes = votes + up_or_down(signature)
        else:  # allow for multiple delegate involvement
            delegated_vote_made = False
            delegated_vote = 0
            for effect in issue_effects:
                for delegatee in delegatees(signer, effect):
                    if delegatee_has_voted:
                        delegated_vote_made = True
                        delegated_vote += delegatee_vote
                    else:  # all applicable delegatees must have voted
                        delegated_vote_made = False
                        break
            if delegated_vote_made:
                turnout += 1
                votes = votes + delegated_vote

Single Issue Delegation
=======================

A group of users create a patch. Everyone likes it and trusts it so they vote to let the group finish it up without any further approval.

This is not possible as a general thing but signers can delegate control of the relevant area/s to users in the group.

Brexit
======

A patch is rejected. What prevents its resubmission and resubmission and resubmission...

Limiting timing for particular users wont work. Is there some way to compare patches for 'similarity'

https://github.com/google/diff-match-patch could be used to compare the patch files. Near matches to proposed, or pending patches would not be accepted into proposed.

Delegate everything
===================

Sorta like today's politics: Tom gives Mary all of his signing rights - he can change this at any time.

Tom creates a delegation_request and Mary accepts it.

Automatic delegation acceptance
===============================

Mary is a politician. She needs to be able to automatically accept all delegation requests.

Selling Votes
=============

The selling of votes is outside of this system - there is no contractual enforcement in the system regarding delegated votes and if a vote is 'bought' somehow, it is up to the seller/buyer to negotiate and contract outside of the system.

That said: A delegator can always see how their vote was used and can take it from the delegator at any time even on a pending issue. The delegatee can see if they lose a delegator but they cannot see which way the delegator voted (if at all).

Fix that typo or grammatical error
==================================

Tom spots a grammar error and decides to fix it.
He clones the documentation and creates a patch with the fix.
He submits the proposed_patch
Nobody can be bothered to pay him any attention because it is such a minor fix.

Tough. The delegation mechanism should ensure that relevant people are focussed on relevant patches.

Club membership
---------------

Roles: New signers automatically delegate their votes according to some template (e.g. All votes to the president)

candidate - signer can become a candidate

candidate_requirements: may need certification (e.g. range_operator)
may need qualification (verified by someone)

Thus if a person becomes an IPSC instructor, this is done by the IPSC captain or president signing a document that ties the person record to the IPSC instructor record (with some date and other data).
Is James an IPSC instructor? - look in the instructors folder for a record containing james and verify its signature.

If a person becomes a member, this is done by the Club secretary or president signing a document that ties the person id to the member document id

