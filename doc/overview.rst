Overview
========

Just like any other git/sphinx project except that we build hooks such that:

A user can vote to accept/reject a pull request.
A user can delegate their vote for content under any folder to another user (and retrieve it at any time)

When a user with delegated votes votes, the delegate votes are also used.

If a pull request content changes, voting is reset - it applies to a specific patch

We fork gitlab and allow the creation of 'democratic repos' where 

Musing
------

A user can look at the documentation in any state in their repo copy. Perhaps badges can be used to show the current
state of the document.

Will need a way to restrict pull request generation. Perhaps an RFC model where some number of votes are needed to
move an RFC into a proposal location...

or consider using the git model of repos such that we just have a few trusted users at this level and their repos control their pull requests etc.
