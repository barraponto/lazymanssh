LAZYMANSSH
==========

You just can't keep typing this, can you? Me neither.


Installing
----------

Just run:
    pip install https://github.com/barraponto/lazymanssh/archive/master.zip

Easy, eh?


Running
-------

Lazymanssh expects the target IPs or domains in a JSON file. This is meant to
leverage the return of `aws describe-instances` calls. You have it installed, *right*?

The basic arguments are:

* `--host`: a prefix for the hostnames. Those will be appended with an index,
  starting at zero, like `myhostname0` or `awesomecluster2`.
* `--user`: a user for ssh logins.
* `--key`: the path to the identity file for logins. Something like `~/.ssh/id_rsa` will work.

Of course, you can always run `lazymanssh --help` and see the help for this command.


Using with AWS CLI
------------------

You're so lazy you're using the CLI for AWS, right? Just pipe the output to
`lazymanssh` -- but keep in mind that the keyword arguments must be in the
command called and it must finish with `-` (it's a lazy way to tell the CLI
you're taking the parameters from stdin). I don't like it either, but I'm 
too lazy to fix it.

Here's a working example:

    aws ec2 describe-instances --filters 'Name=tag:Name,Values=LAB*' \
    --query 'Reservations[*].Instances[*].PublicIpAddress[]' | lazymanssh \
    --host labcluster --user ubuntu --key ~/.ssh/lab.pem -
