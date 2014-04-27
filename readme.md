passpy
=======

This is a simple password generator, it will generate passwords based on
hash of salt and phrase combination. This way, you can easily manage
different passwords for various services with just memorizing the
phrase.

To create a new password, run:

    pass.py -n

At first it will find a salt file at `~/.saltpass`, if not exists, it
will ask you for a default salt, but you can always customize the salt
afterwards.

The command above will then ask you for the phrase, and then copy the
generated password to clipboard without printing it to stdout. You can
then paste it to anywhere. Please note that copying to cipboard currently
only works on Mac, to see the generated password, you can pass `-o`
option.

The `-n` option on the above command will simply confirm the pharse to
avoid typos. This is good when you are creating new password, like when
you are about to register/change your password on some services. If you
just want to generate a password, run `pass.py` without any options.

In case you want to customize the salt, pass the `-s` option, the
command will then ask you for a custom salt before asking for phrase.
You can also combine this with `-n` option.

In the case of password length-limit, you can pass `-l <length>`
argument to set the final length of the password, for example:

    pass.py -l 10

Todo:
------

* Confirm custom salt on `-n` mode.
* Make hash algorithm customizable
* Make SUFFIX customizable
* Change `.saltpass` filename to something more relevant
* Support clipboard on Windows and Linux machines
