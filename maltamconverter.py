import malconverter


class MalayalamToTamilConverter(malconverter.LangConverter):
    mal_tamil_map = {
        u'\u0d00': '',
        u'\u0d01': '',
        u'\u0d02': u'\u0bae\u0bcd',  # anuswaram
        u'\u0d03': u'\u0b83',  # visarggam
        u'\u0d04': '',
        u'\u0d05': u'\u0b85',  # അ
        u'\u0d06': u'\u0b86',  # ആ
        u'\u0d07': u'\u0b87',  # ഇ
        u'\u0d08': u'\u0b88',  # ഈ
        u'\u0d09': u'\u0b89',  # ഉ
        u'\u0d0a': u'\u0b8a',  # ഊ
        u'\u0d0b': u'\u0b87\u0bb1\u0bc1',  # ഋ
        u'\u0d0c': '',  # ഌ
        u'\u0d0d': '',
        u'\u0d0e': u'\u0b8e',  # എ
        u'\u0d0f': u'\u0b8e',  # ഏ

        u'\u0d10': u'\u0b90',  # ഐ
        u'\u0d11': '',
        u'\u0d12': u'\u0b92',  # ഒ
        u'\u0d13': u'\u0b93',  # ഓ
        u'\u0d14': u'\u0b94',  # ഔ
        u'\u0d15': u'\u0b95',  # ക
        u'\u0d16': u'\u0b95',  # ഖ
        u'\u0d17': u'\u0b95',  # ഗ
        u'\u0d18': u'\u0b95',  # ഘ
        u'\u0d19': u'\u0b99',  # ങ
        u'\u0d1a': u'\u0b9a',  # ച
        u'\u0d1b': u'\u0b9a',  # ഛ
        u'\u0d1c': u'\u0b9c',  # ജ
        u'\u0d1d': u'\u0b9a',  # ഝ
        u'\u0d1e': u'\u0b9e',  # ഞ
        u'\u0d1f': u'\u0b9f',  # ട

        u'\u0d20': u'\u0b9f',  # ഠ
        u'\u0d21': u'\u0b9f',  # ഡ
        u'\u0d22': u'\u0b9f',  # ഢ
        u'\u0d23': u'\u0ba3',  # ണ
        u'\u0d24': u'\u0ba4',  # ത
        u'\u0d25': u'\u0ba4',  # ഥ
        u'\u0d26': u'\u0ba4',  # ദ
        u'\u0d27': u'\u0ba4',  # ധ
        u'\u0d28': u'\u0ba8',  # ന
        u'\u0d29': u'\u0ba9',  # ഩ
        u'\u0d2a': u'\u0baa',  # പ
        u'\u0d2b': u'\u0baa',  # ഫ
        u'\u0d2c': u'\u0baa',  # ബ
        u'\u0d2d': u'\u0baa',  # ഭ
        u'\u0d2e': u'\u0bae',  # മ
        u'\u0d2f': u'\u0baf',  # യ

        u'\u0d30': u'\u0bb0',  # ര
        u'\u0d31': u'\u0bb1',  # റ
        u'\u0d32': u'\u0bb2',  # ല
        u'\u0d33': u'\u0bb3',  # ള
        u'\u0d34': u'\u0bb4',  # ഴ
        u'\u0d35': u'\u0bb5',  # വ
        u'\u0d36': u'\u0bb6',  # ശ
        u'\u0d37': u'\u0bb7',  # ഷ
        u'\u0d38': u'\u0bb8',  # സ
        u'\u0d39': u'\u0bb9',  # ഹ
        u'\u0d3a': '',
        u'\u0d3b': '',
        u'\u0d3c': '',
        u'\u0d3d': '',
        u'\u0d3e': u'\u0bbe',  # aa
        u'\u0d3f': u'\u0bbf',  # i

        u'\u0d40': u'\u0bc0',  # ii
        u'\u0d41': u'\u0bc1',  # u
        u'\u0d42': u'\u0bc2',  # uu
        u'\u0d43': u'\u0bbf\u0bb1\u0bc1',  # R
        u'\u0d44': '',  # RR
        u'\u0d45': '',
        u'\u0d46': u'\u0bc6',  # e
        u'\u0d47': u'\u0bc7',  # E
        u'\u0d48': u'\u0bc8',  # ai
        u'\u0d49': '',
        u'\u0d4a': u'\u0bca',  # o
        u'\u0d4b': u'\u0bcb',  # O
        u'\u0d4c': u'\u0bcc',  # au
        u'\u0d57': u'\u0bcc',  # au
        u'\u0d4d': u'\u0bcd',  # virama
        u'\u0d4e': '',
        u'\u0d4f': '',

        u'\u0d50': '',
        u'\u0d51': '',
        u'\u0d52': '',
        u'\u0d53': '',
        u'\u0d54': '',
        u'\u0d55': '',
        u'\u0d56': '',
        u'\u0d58': '',
        u'\u0d59': '',
        u'\u0d5a': '',
        u'\u0d5b': '',
        u'\u0d5c': '',
        u'\u0d5d': '',
        u'\u0d5e': '',
        u'\u0d5f': '',

        u'\u0d60': '',
        u'\u0d61': '',
        u'\u0d62': '',
        u'\u0d63': '',
        u'\u0d64': '',
        u'\u0d65': '',
        u'\u0d66': '',  # 0
        u'\u0d67': '',  # 1
        u'\u0d68': '',  # 2
        u'\u0d69': '',  # 3
        u'\u0d6a': '',  # 4
        u'\u0d6b': '',  # 5
        u'\u0d6c': '',  # 6
        u'\u0d6d': '',  # 7
        u'\u0d6e': '',  # 8
        u'\u0d6f': '',  # 9

        u'\u0d70': '',
        u'\u0d71': '',
        u'\u0d72': '',
        u'\u0d73': '',
        u'\u0d74': '',
        u'\u0d75': '',
        u'\u0d76': '',
        u'\u0d77': '',
        u'\u0d78': '',
        u'\u0d79': '',
        u'\u0d7a': u'\u0ba3\u0bcd',  # ൺ
        u'\u0d7b': u'\u0ba9\u0bcd',  # ൻ
        u'\u0d7c': u'\u0bb0\u0bcd',  # ർ
        u'\u0d7d': u'\u0bb2\u0bcd',  # ൽ
        u'\u0d7e': u'\u0bb3\u0bcd',  # ൾ
        u'\u0d7f': u'\u0b95\u0bcd',  # ൿ

    }

    def __init__(self):
        super().__init__(self.mal_tamil_map)


if __name__ == '__main__':
    c = MalayalamToTamilConverter()
    print(c.convert_line('ഗണപതി'))

    c.convert('/Users/umesh.nair/Downloads/mal_song.txt', '/Users/umesh.nair/Downloads/tam_song.txt')