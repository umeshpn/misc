class WordleSolver:

    def __init__(self, n_letters):
        self.n_letters = n_letters
        self.candidate_words = None
        self.all_words = None
        self.suggest_next_word = True
        self.list_all_words = True
        self.use_full_dict = True

        self.full_dict_guesses = dict()
        self.candidate_dict_guesses = dict()

        self.remaining_words = None

    def set_dictionaries(self, candidate_dict, additional_dict):
        self.candidate_words = sorted(list(set(candidate_dict)))
        self.all_words = sorted(list(set(candidate_dict).union(set(additional_dict))))
        self.initialize_words()

    def initialize_words(self):
        self.remaining_words = list(self.candidate_words)

    def get_response(self, word, master_word):
        response = ''
        letter_count = dict()
        for i in range(self.n_letters):
            letter_count[master_word[i]] = letter_count.get(master_word[i], 0) + 1
        # print(letter_count)
        for i in range(self.n_letters):
            if word[i] == master_word[i]:
                response += 'G'
                letter_count[word[i]] -= 1
            elif word[i] in master_word and letter_count.get(word[i], 0) > 0:
                response += 'Y'
                letter_count[word[i]] -= 1
            else:
                response += 'B'
        return response

    def purge(self, word, result):
        word = word.lower()
        result = result.upper()
        new_remaining_words = set(self.remaining_words)
        for dict_word in list(self.remaining_words):
            yes_no = self.check_fails(dict_word, word, result)
            if yes_no:
                # print('Check failed for dict word = %s, word = %s, result = %s' % (dict_word, word, result))
                new_remaining_words.remove(dict_word)
            # else:
                # print('Check OK  for dict word = %s, word = %s, result = %s' % (dict_word, word, result))
        self.remaining_words = new_remaining_words

    def check_fails(self, dict_word, word, result):
        # print(dict_word, word, result)
        unmatched_letters = dict()
        for i in range(self.n_letters):
            dict_letter = dict_word[i]
            word_letter = word[i]
            # print(dict_letter, word_letter)
            if dict_letter == word_letter and result[i] != 'G':
                return True
            if result[i] == 'G' and dict_letter != word_letter:
                return True
            if result[i] != 'G' and dict_letter != word_letter:
                if dict_letter in unmatched_letters:
                    unmatched_letters[dict_letter] += 1
                else:
                    unmatched_letters[dict_letter] = 1

        # print(unmatched_letters)
        for i in range(self.n_letters):
            word_letter = word[i]
            if result[i] == 'Y':
                if word[i] not in unmatched_letters:
                    return True
                if unmatched_letters[word[i]] > 0:
                    unmatched_letters[word[i]] -= 1
                else:
                    return True
            elif result[i] == 'B':
                if word[i] in unmatched_letters and unmatched_letters[word[i]] > 0:
                    return True
        return False


    def play(self):
        self.initialize_words()
        self.list_all_words = True
        self.known_letters = set()
        response = 'XXXXX'
        guess_no = 0
        while response != 'GGGGG':
            guess_no += 1
            guess = input("Guess %d: " % guess_no)
            response = input('Response: ')
            self.purge(guess, response)
            if self.list_all_words:
                print('%d: %s' % (len(self.remaining_words), self.remaining_words))
                # print("Suggested words: %s" % self.get_suggested_words())

    # def get_suggested_words(self):
    #     unknown_letters = self.gather_letters()
    #     self.print_non_candidates(unknown_letters)
    #
    # def gather_letters(self):
    #     unknown_letters = set()
    #     for word in self.remaining_words:
    #         for letter in word:
    #             if letter not in self.known_letters:
    #                 unknown_letters.add(letter)
    #
    def do_trial(self, master_word, start_word):
        self.initialize_words()
        response = 'BBBBB'
        guess_count = 0
        if start_word:
            next_word = start_word
        else:
            next_word = self.best_guess()
        sequence = '%d' % len(self.remaining_words)
        while response != 'GGGGG':
            guess_count += 1
            response = self.get_response(next_word, master_word)
            print('Guess %d = %s, Response = %s' % (guess_count, next_word, response))

            if response == 'GGGGG':
                return guess_count, next_word, sequence

            if len(self.remaining_words) < 2:
                return 0, None, ''

            self.purge(next_word, response)
            # if len(self.remaining_words) < 10:
            #     print('# of words = %d, Words = %s' % (len(self.remaining_words), self.remaining_words))
            # else:
            #     print('# of words = %d' % len(self.remaining_words))
            next_word = self.best_guess()
            sequence += ' $\Rightarrow$ %d' % len(self.remaining_words)
            if self.list_all_words:
                print('%d: %s' % (len(self.remaining_words), self.remaining_words))

    def best_guess(self):
        if len(self.remaining_words) == 0:
            raise "No solution."
        if len(self.remaining_words) < 3:
            return list(self.remaining_words)[0]

        best = len(self.remaining_words) + 1
        best_strings = []

        # Inspect each word in the dictionary (including non-candidate words)
        if self.use_full_dict:
            words_to_iterate = self.candidate_words
        else:
            words_to_iterate = self.remaining_words
        for dict_word in words_to_iterate:
            response_counts = dict()

            # Compare the dictionary word with each of the candidate word,
            # and collect response for each of them, considering the dictionary word as the guess
            # and the candidate word as the answer.
            # Collect the count of each response there.
            for rem_word in self.remaining_words:
                response = self.get_response(dict_word, rem_word)
                if response in response_counts:
                    response_counts[response] += 1
                else:
                    response_counts[response] = 1
                # print(response_counts)

            # Now, find which of these responses
            worst = 0
            for response in response_counts.keys():
                count = response_counts[response]
                if worst < count:
                    worst = count
            if worst < best:
                best = worst
                best_strings.clear()
                best_strings.append(dict_word)
            elif worst == best:
                best_strings.append(dict_word)
            # print("dict_word = %s, best so far = %d" % (dict_word, best))

        next_guess = best_strings[0]
        return next_guess

    def print_non_candidates(self, letters):
        letters = letters.lower()
        word_dict = dict()
        for dict_word in list(self.candidate_words):
            count = 0
            for letter in letters:
                if letter in dict_word:
                    count += 1
            if count > 2:
                word_dict[dict_word] = count
        words = list(word_dict.keys())
        words.sort(key=lambda x : (-word_dict[x], x))
        matches = 100
        for word in words:
            count = word_dict[word]
            if count != matches:
                matches = count
                print('Count : %d' % count)
            print('         %s' % word)
    def do_trials(self, master_word, start_words):
        # print('\nMaster word = %s' % master_word)
        start_word_map = dict()
        sequence_map = dict()
        for start_word in start_words:
            # print('\nStart word = %s' % start_word)
            n, w, sequence = ws.do_trial(master_word, start_word)
            if w:
                # print('word = %s' % w)
                start_word_map[start_word] = n
                sequence_map[start_word] = sequence
            else:
                print('Could not find the solution.')
        sorted_start_words = list(start_word_map.keys())
        sorted_start_words.sort(key=lambda x : (start_word_map[x], x))
        # print('\n\nResults:')
        print('\\begin{tabular}{|c|c|l|}')
        print('\\hline')
        print('\\textbf{Start} & \\textbf{\\#} & \\textbf{Progression}\\\\')
        print('\\hline')
        n_words = 0
        n_trials = 0
        for w in sorted_start_words:
            n_guesses = start_word_map[w]
            print('%s & %d & (%s) \\\\' % (w, n_guesses, sequence_map[w]))
            n_words += 1
            n_trials += n_guesses
            if self.use_full_dict:
                d = self.full_dict_guesses
            else:
                d = self.candidate_dict_guesses
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        print('\\hline')
        print('\\textbf{Mean} & %.2f & \\\\' % (n_trials * 1.0 / n_words))
        print('\\hline')
        print('\\end{tabular}')

    def do_two_trials(self, master_word, start_words):
        print('\\subsection{Answer = %s}\n\n' % master_word)
        print('\\begin{table}[H]')
        print('\\begin{tabular}{cc}')
        print('\\textbf{Using full words} & \\textbf{Using candidate words}\\\\')
        self.use_full_dict = True
        self.do_trials(master_word, start_words)
        print('&')
        self.use_full_dict = False
        self.do_trials(master_word, start_words)
        print('\\end{tabular}')
        print('\\caption{Solving the word %s}' % master_word)
        print('\\end{table}')

        self.full_start_words = list(start_words.keys())
        self.full_start_words.sort(key=lambda x : (self.full_start_words[x], x))

        self.cand_start_words = list(start_words.keys())
        self.cand_start_words.sort(key=lambda x : (self.cand_start_words[x], x))



def test_get_response(ws):
    test_data = [
        ['raise', 'picky', 'BBYBB'],
        ['sheep', 'level', 'BBYGB'],
        ['sheep', 'pests', 'YBYBY']
    ]

    for data in test_data:
        candidate, master, expected_result = data[0], data[1], data[2]
        act = ws.get_response(candidate, master)
        if act != expected_result:
            print("Candidate = %s, Master = %s, Actual response = %s, Expected Response = %s" % (candidate, master, act, expected_result))


if __name__ == '__main__':
    ws = WordleSolver(5)
    test_get_response(ws)