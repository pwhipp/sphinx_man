Implementation
==============

We're building a protected_repository. Changes can only be made to the repository that satisfy the signing rules within the protected_repository (the signing rules themselves are covered by themselves).

To get started, we'll view the basic database as a git repository protected by a push hook that invokes a python governor.
The governor will only allow the push if the push is permitted according to the .signing_rules relating to its content.

The general file representation for data will be yaml and the canonical name of any entity will be reflected by its full path name.

We need database functionality for users, signatures etc. and have been thinking about mongodb but we also need the signing to apply to this.
If we're implementing the signing and verification in python in a git hook we don't really want the risk of a parallel implementation in mongodb (or an api layer to it). Instead, the mongo db is read only to the outside world and is affected only by changes that are written to the git repository and are subject to the signing rules. We can have multiple databases under /databases in git. Each db can have multiple collections e.g. /databases/main/people/

Is there any reason to put all this in the git repository or should we use lots of repositories/databases?

Microservice approach??

Starting with a repo created that sets up a git hook that passes any pushed changes to a python function. The changes are in the form of a list of files changed, files added and files deleted. For the file changes we may also need the diff.

The function will return true if the push is permitted, false otherwise. (Initially just a stub returning False to reject all pushes).

Then we can ensure that the 'push_info' is relevant to the 'signing_rules' language/specification.

First step is to use the pre_receive hook to reject a push attempt that does not contain the required signatures.
Next step is to use mostly the same code in pre_push to prevent the push attempt from taking place.

Privacy
-------

Break up data and encrypt. key subject to .privacy_rules?

Encrypt is somewhat tricky if we want to use a similar rule spec idea because there would have to be a 'trusted' man in the middle
who uses the rules to decide if a particular user can receive the content. Furthermore, we'd want their 'view' of the data to indicate that it was encrypted so that they are less likely to inadvertently share it.

Anonymity
---------

Maybe just through privacy?


Thoughts
--------

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

