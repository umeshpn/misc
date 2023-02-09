
class ChuplaVideoLister:
    def __init__(self):
        self.place_people_map = dict()

    def parse_csv(self, csv_file):
        with open(csv_file, 'r') as in_file:
            for line in in_file.readlines():
                line = line[:-1]
                name, country, video = line.split(',')
                if video == 'Y' or video == 'y':
                    if country in self.place_people_map:
                        people = self.place_people_map[country]
                        people.append(name)
                    else:
                        people = [name]
                        self.place_people_map[country] = people
        # print(self.place_people_map)

    def print_details(self):
        n_people = 0
        for country in sorted(self.place_people_map.keys()):
            people = self.place_people_map[country]
            print ('\nRegion: %s (%d)' % (country, len(people)))
            n_people += len(people)
            for person in sorted(people):
                print('    - %s' % person)
        print('\nTOTAL = %d' % n_people)


if __name__ == '__main__':
    cvl = ChuplaVideoLister()
    cvl.parse_csv('/Users/umesh.nair/Downloads/chuplans-sandhya.csv')
    cvl.print_details()
