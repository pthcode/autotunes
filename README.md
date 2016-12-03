# autotunes #

Automate your music uploads.

### How does autotunes work? ###

* Scans through your music directory, looking for matching albums on MusicBrainz.
* When it finds a match, it will ask you to select the correct release.
* After you choose a release, it will create a torrent, grab tags from last.fm, find album artwork, and upload to PTH automatically.
* When it doesn't find a match, you can manually select the correct MusicBrainz release group before uploading.

### How do I get set up? ###

1. Install Python 3.
2. Clone the repository with `git clone https://github.com/pthcode/autotunes.git && cd autotunes`.
3. Install the dependencies with `pip3 install -r requirements.txt`.
4. Run `python3 ./autotunes.py -o <watch_dir> <username> /path/to/album`, enter your password, and autotunes will do its magic. You can specify multiple albums at a time.

### Disclaimer ###

* Dupe-checking is not yet implemented.
* autotunes is provided for demonstration purposes only.

### Roadmap ###

* Discogs support.
* Improved matching function which takes .log and .cue files, catalog numbers and years in folder names, and file types into account.
