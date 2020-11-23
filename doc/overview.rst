Overview
========

Just like any other git/sphinx project except that we build hooks such that:

A user can vote to accept/reject a pull request.
A user can delegate their vote for content under any folder to another user (and retrieve it at any time)

When a user with delegated votes votes, the delegate votes are also used.

If a pull request content changes, voting is reset - it applies to a specific patch

Musing
------
A 'voting rules' meta maybe? Some sort of .voting_rules file that goes in a folder and affects the file changes in that folder and its subfolders. These would need to be merge-able for any given patch.

Need a period for voting. Maybe make this voting dependent - e.g. 1 week from last vote is when request is accepted or rejected.

Will need a way to restrict pull request generation. Perhaps an RFC model where some number of votes are needed to
move an RFC into a proposal location...

or consider using the git model of repos such that we just have a few trusted users at this level and their repos control their pull requests etc.
