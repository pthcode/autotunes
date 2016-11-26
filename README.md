# autotunes #

Automate your music uploads.

### How does autotunes work? ###

* Scans through your music directory, looking for matching albums on MusicBrainz.
* When it finds a perfect match, it will create a torrent and upload to PTH automatically.
* When it finds a high-confidence match, it will ask for your confirmation before uploading.
* When it doesn't find a match, you can manually select the correct MusicBrainz release before uploading.

### How do I get set up? ###

1. Install Python 2.
2. Install autotunes and its dependencies with `sudo pip2 install </path/to/autotunes>`.
3. Run `autotunes`, and `~/.config/autotunes/autotunes.ini` will be created. Fill it out with your information.
4. Run `autotunes /path/to/album`, and autotunes will do its magic. You can specify multiple albums at a time.