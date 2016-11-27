# autotunes #

Automate your music uploads.

### How does autotunes work? ###

* Scans through your music directory, looking for matching albums on MusicBrainz.
* When it finds a match, it will ask you to select the correct release.
* After you choose a release, it will create a torrent, grab tags from last.fm, find album artwork, and upload to PTH automatically.
* When it doesn't find a match, you can manually select the correct MusicBrainz release group before uploading.

### How do I get set up? ###

1. Install Python 3.
2. Install the latest version of mktorrent from https://github.com/Rudde/mktorrent.
3. Install autotunes and its dependencies with `sudo pip install </path/to/autotunes>`.
4. Run `autotunes -o <watch_dir> <username> /path/to/album`, enter your password, and autotunes will do its magic.
5. You can specify multiple albums at a time.
