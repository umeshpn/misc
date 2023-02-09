
class SanthaBuddyLister:

    def __init__(self):
        self.santa_buddy_map = dict()
        self.persons = set()

    def parse_file(self, filename):
        with open(filename, 'r') as infile:
            for line in infile.readlines():
                line = line[:-1]
                # print(line)
                santa, buddy = line.split(',')
                self.persons.add(santa)
                self.persons.add(buddy)
                self.santa_buddy_map[santa] = buddy

    def print_chain(self):
        done = False
        while not done:
            if len(self.persons) == 0:
                break
            santa = self.persons.pop()
            self.persons.add(santa)
            print(santa)
            while santa:
                if santa not in self.persons:
                    break
                done = True
                self.persons.remove(santa)
                buddy = self.santa_buddy_map[santa]
                if buddy:
                    print('     => %s' % buddy)
                    santa = buddy
                    done = False
                else:
                    print('No buddy for %s' % santa)
                    break


if __name__ == '__main__':
    sml = SanthaBuddyLister()
    # sml.parse_file('/Users/umesh.nair/Downloads/2021-Chupla-Santa-Buddy-List.csv')
    sml.parse_file('/Users/umesh.nair/Downloads/2022-Chupla-Santa-Buddy-List.csv')
    print(sml.santa_buddy_map)
    sml.print_chain()
