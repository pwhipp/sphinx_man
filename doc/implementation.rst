Implementation
==============

To get started, we'll view the basic database as a git repository protected by a push hook that invokes a python governor.
The governor will only allow the push if the push is permitted according to the .signing_rules relating to its content.

The general file representation for data will be yaml and the canonical name of any entity will be reflected by its data file location.
Type may be inferred from the location or from the data itself.

Maybe make this a mongodb thing. The patchrules application will apply or reject patches.
Make it sit alongside a repo? Make Mongo the repo?? We could sorta write git in mongodb if we wanted to... why?

If I make mongodb the repo then I'll need to be able to publish the canonical document and, with patches, publish the 'diff' version in a nice way - not just the new version, a sphinx document that shows added/removed/changed sections.

Ethereum 2 is another interesting possibility.

In order to try to make this a decision that can be changed for relatively low cost while prototyping, I'll aim to abstract things so that there is the sorta equivalent of an ORM layer.

python's marshmallow library might offer better schema control and validation than mongo's built in stuff.

Signing what??
--------------

In this system a vote is fundamentally a signature on a patch. Once the patch is applied TheBook is updated.

We're going to need a 'blame' system to allow the history of changes to lines to be tracked but we also need to consider how this applies to data. Git already has blame features, history etc. and is an appealing underlying application.

