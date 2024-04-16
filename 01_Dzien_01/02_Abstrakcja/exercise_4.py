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


class Questionnaire(SingleChoiceQuestion):
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        for i in self.questions:
            i.ask()


questionnaire = Questionnaire('Ankieta dotycząca zadowolenia z wyboru laptopa')

q1 = SingleChoiceQuestion('Matryca', ['mniej niż 15 cali', 'od 15 do 17 cali', 'więcej niż 17 cali'])

q2 = SingleChoiceQuestion('Rodzaj ekranu', ['matowy', 'błyszczący'])

q3 = SingleChoiceQuestion('Czy polecisz go znajomemu?',
                          ['zdecydowanie tak', 'raczej tak', 'nie mam zdania', 'raczej nie', 'zdecydowanie nie'])

questionnaire.add_question(q1)
questionnaire.add_question(q2)
questionnaire.add_question(q3)
answers = questionnaire.run()
