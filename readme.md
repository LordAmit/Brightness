# Why this branch

The code is kept in this format in order to make .deb package and upload it to the [ppa](https://launchpad.net/~apandada1/+archive/ubuntu/brightness-controller).

# Instructions for packaging 

- create gpg and ssh keys (if not already done)
- upload keys to launchpad (if not already done)
- go to the repository, run `dch`
- update changelog in nano
- run `debuild` (to create a .deb file for testing)
- test the build 
- run `debuild -S` (to generate the .source.changes file)
- to upload run `dput ppa:user-name/ppa-name name.source.changes`