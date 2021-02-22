# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = '_'*len(self.word)

    def guess(self, char):

        if self.status != STATUS_ONGOING:
            raise ValueError('game ended')

        # check if the letter has been correctly guessed already
        if char in self.masked_word:
            self.remaining_guesses -= 1
            return

        # check if the guess is correct
        if char in self.word:
            word_list = list(zip(self.word, self.masked_word))
            self.masked_word = ''
            for let in word_list:
                self.masked_word += let[0] if char == let[0] else let[1]
            if '_' not in self.masked_word:
                self.status = STATUS_WIN
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status
