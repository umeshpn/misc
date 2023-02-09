import malconverter


class MalayalamToRomanConverter(malconverter.LangConverter):
    mal_roman_map = {
        u'\u0d00': '',
        u'\u0d01': '',
        u'\u0d02': u'\u1e41',  # anuswaram
        u'\u0d03': u'\u1e25',  # visarggam
        u'\u0d04': '',
        u'\u0d05': 'a',  # അ
        u'\u0d06': u'\u0101',  # ആ
        u'\u0d07': 'i',  # ഇ
        u'\u0d08': u'\u012b',  # ഈ
        u'\u0d09': 'u',  # ഉ
        u'\u0d0a': u'\u016b',  # ഊ
        u'\u0d0b': u'r\u0325',  # ഋ
        u'\u0d0c': u'r\u0325',  # ഌ
        u'\u0d0d': '',
        u'\u0d0e': 'e',  # എ
        u'\u0d0f': u'\u0113',  # ഏ

        u'\u0d10': 'ai',  # ഐ
        u'\u0d11': '',
        u'\u0d12': 'o',  # ഒ
        u'\u0d13': u'\u014d',  # ഓ
        u'\u0d14': 'au',  # ഔ
        u'\u0d15': 'kQ',  # ക
        u'\u0d16': 'khQ',  # ഖ
        u'\u0d17': 'gQ',  # ഗ
        u'\u0d18': 'ghQ',  # ഘ
        u'\u0d19': u'\u1e45Q',  # ങ
        u'\u0d1a': 'cQ',  # ച
        u'\u0d1b': 'chQ',  # ഛ
        u'\u0d1c': 'jQ',  # ജ
        u'\u0d1d': 'jhQ',  # ഝ
        u'\u0d1e': u'\u00f1Q',  # ഞ
        u'\u0d1f': u'\u1e6dQ',  # ട

        u'\u0d20': u'\u1e6dhQ',  # ഠ
        u'\u0d21': u'\u1e0dQ',  # ഡ
        u'\u0d22': u'\u1e0dhQ',  # ഢ
        u'\u0d23': u'\u1e47Q',  # ണ
        u'\u0d24': 'tQ',  # ത
        u'\u0d25': 'thQ',  # ഥ
        u'\u0d26': 'dQ',  # ദ
        u'\u0d27': 'dhQ',  # ധ
        u'\u0d28': 'nQ',  # ന
        u'\u0d29': 'Q',  # ഩ
        u'\u0d2a': 'pQ',  # പ
        u'\u0d2b': 'phQ',  # ഫ
        u'\u0d2c': 'bQ',  # ബ
        u'\u0d2d': 'bhQ',  # ഭ
        u'\u0d2e': 'mQ',  # മ
        u'\u0d2f': 'yQ',  # യ

        u'\u0d30': 'rQ',  # ര
        u'\u0d31': 'rQ',  # റ
        u'\u0d32': 'lQ',  # ല
        u'\u0d33': 'lQ',  # ള
        u'\u0d34': 'Q',  # ഴ
        u'\u0d35': 'vQ',  # വ
        u'\u0d36': u'\u015bQ',  # ശ
        u'\u0d37': u'\u1e63Q',  # ഷ
        u'\u0d38': 'sQ',  # സ
        u'\u0d39': 'hQ',  # ഹ
        u'\u0d3a': '',
        u'\u0d3b': '',
        u'\u0d3c': '',
        u'\u0d3d': '',
        u'\u0d3e': u'\u0101',  # aa
        u'\u0d3f': 'i',  # i

        u'\u0d40': u'\u012b',  # ii
        u'\u0d41': 'u',  # u
        u'\u0d42': u'\u016b',  # uu
        u'\u0d43': u'r\u0325',  # R
        u'\u0d44': '',  # RR
        u'\u0d45': '',
        u'\u0d46': 'e',  # e
        u'\u0d47': u'\u0113',  # E
        u'\u0d48': 'ai',  # ai
        u'\u0d49': '',
        u'\u0d4a': 'o',  # o
        u'\u0d4b': u'\u014d',  # O
        u'\u0d4c': 'au',  # au
        u'\u0d57': 'au',  # au
        u'\u0d4d': 'x',  # virama
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
        u'\u0d7a': u'\u1e47',  # ൺ
        u'\u0d7b': 'n',  # ൻ
        u'\u0d7c': 'r',  # ർ
        u'\u0d7d': 'l',  # ൽ
        u'\u0d7e': 'l',  # ൾ
        u'\u0d7f': 'k',  # ൿ

    }

    def __init__(self):
        super().__init__(self.mal_roman_map)

    def second_pass(self, line):
        for vowel in [u'\u0101', 'i', u'\u012b', 'u', u'\u016b', u'r\u0325', 'e', u'\u0113', 'ai', 'o', u'\u014d', 'au']:
            line = line.replace('Q%s' % vowel, vowel)
        return line.replace('Qx', ''). replace('Q', 'a')


if __name__ == '__main__':
    c = MalayalamToRomanConverter()
    print(c.convert_line('ഗണപതി'))

    c.convert('/Users/umesh.nair/Downloads/mal_song.txt', '/Users/umesh.nair/Downloads/rom_song.txt')