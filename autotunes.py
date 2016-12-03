#!/usr/bin/env python
import argparse
import libpth.api
import libpth.identify
import libpth.tagging
import libpth.utils


def upload_release(release, api, data_dir=None, torrent_dir=None):
    release.artwork_url = libpth.identify.fetch_artwork(release)
    release.tags = libpth.identify.fetch_tags(release)
    if len(release.tags) == 0:
        release.tags = input('tags: ').split(', ')
    libpth.tagging.apply_metadata(release)
    libpth.tagging.fix_release_filenames(release, directory=data_dir)
    release.torrent = libpth.utils.make_torrent(release.path, api.passkey, output_dir=torrent_dir)
    api.upload(release, 'Uploaded with [url=https://github.com/pthcode/autotunes]autotunes[/url].')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('username')
    parser.add_argument('-d', '--data-dir',
                        help='the directory where data will be output')
    parser.add_argument('-o', '--torrent-dir',
                        help='the directory where torrents will be output',
                        default='/srv/torrents')
    parser.add_argument('album', help='path to the album(s) you want to upload', nargs='+')
    args = parser.parse_args()
    password = input('password: ')
    api = libpth.api.API(args.username, password)
    libpth.identify.identify_releases(args.album, callback=lambda release:
                                      upload_release(release, api, args.data_dir, args.torrent_dir))


if __name__ == '__main__':
    main()
