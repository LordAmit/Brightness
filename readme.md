# Why this branch

The code is kept in this format in order to make .deb package and upload it to the [ppa](https://launchpad.net/~apandada1/+archive/ubuntu/brightness-controller).

# Instructions for packaging 

- create gpg and ssh keys (if not already done)
- `ssh-keygen`
- gpg --send-keys --keyserver keyserver.ubuntu.com $GPGKEY(8letter)
- upload keys to launchpad (if not already done)
- To decrypt message, save the message in a file and use `gpg -d /path/to/that/file`
- ssh key is located at `.ssh/id_rsa.pub`
- update the release branch from master
- go to the directory, run `dch`
- update changelog in nano
- run `debuild` (to create a .deb file for testing)
- test the build
- run `debuild -S` (to generate the .source.changes file)
- to upload run `dput ppa:user-name/ppa-name name.source.changes`