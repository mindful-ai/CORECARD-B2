import random

class wordjumble:

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.L = ["apples", "laptop", "airplane", "india", "elephant", "mobile", "pencil", "computer", "banana"]

    def jumble(self, word):
        temp = list(word)
        random.shuffle(temp)
        return ''.join(temp)

    def run(self):
        print('Starting: ', self.name)
        print('-'*60)
        random.shuffle(self.L)
        # Repeat the following for entire list
        for word in self.L:

            # Choose a word randomly
            # Shuffle the characters in the word
            jword = self.jumble(word)

            # Show it to the user and take the input
            print("Can you guess this word -> ", jword)
            uinput = input("-> ")

            # Check if the input is correct or not
            # Based on that award point
            if(uinput == word):
                self.points += 1
                print("Correct")
            else:
                print("Incorrect")

            print('-' * 60 + '\n')

    def results(self):
        print(self.name, ", Your score ", self.points, '/', len(self.L))



# ====================================================

p1 = wordjumble('Anil')
p2 = wordjumble('Sunil')


p1.run()
p2.run()

p1.results()
p2.results()