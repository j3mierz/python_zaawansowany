class Questionnaire:
    def __init__(self):
        pass

class SingleChoiceQuestion:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def ask(self):
        print(self.question)
        character = 97
        user = []
        for i in self.answers:
            print(f'{chr(character)}) {i}')
            user.append(chr(character))
            character += 1
        print()
        result = input()
        while result not in user:
            print('Please enter a valid answer!!!')
            result = input()
        return self.answers[user.index(result)]


a = SingleChoiceQuestion('Welcome to Pytho?n', ['sie', 'sdd', 'sds', 'd2d3'])
print(a.ask())