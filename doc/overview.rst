Overview
========

Democratic, hassle free collaborative management of any sized group for teams, clubs, organizations, countries, worlds, solar systems, galaxies...

If only there was an easy way to
  - See all of our legislation/documentation
  - see all proposed changes
  - vote on any changes that interest us
  - delegate my vote to people I trust (and get my vote back whenever I want)


When the going's good, I don't have to do anything. If I have an issue I can easily raise it. If I want to vote on anything in particular, I can.

It starts with names
====================

The entities in the system are
signers (people),
documents (legislation),
proposed changes (patches),
roles (president etc.)

All entities share the same name space which is a hierarchical structure. Each entity has only one name in this space but
it may allow for aliases and tagging.

Thus there can only be one /people/smith_john_99.yaml etc.

Regular expressions may refer to groups of entities which are automatically expanded when they occur in lists.


If I sign something and that thing changes then my signature is invalidated. Therefore we aim to have small relatively
immutable packages of data that we relate using the signatures.

