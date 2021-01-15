import random


class Game:
    def __init__(self):
        self.new_card = []
        self.lotto = []

    def generate_card(self):
        while len(self.new_card) != 15:
            i = random.randint(1, 90)
            if i not in self.new_card:
                self.new_card.append(i)
        return sorted(self.new_card)

    def generate_lotto(self):
        self.lotto = [i for i in range(1, 91)]
        return self.lotto

    @staticmethod
    def show_card(card, whose_card):
        print('''
                -------{} card-------
                   {} {} {}      {} {}
                 {}   {} {}  {}  {}   
                   {} {} {}  {}     {}
                -----------------------
                '''.format(whose_card, card[0], card[1], card[2], card[3], card[4], card[5], card[6],
                           card[7], card[8], card[9], card[10], card[11], card[12], card[13], card[14]))


class Play:
    def __init__(self):
        self.comp_number_matches = 0
        self.player_number_matches = 0
        self.player_card = Game().generate_card()
        self.comp_card = Game().generate_card()
        self.lotto = Game().generate_lotto()
        self.random_number = None

    def show_new_number(self):
        self.random_number = random.choice(self.lotto)
        self.lotto.remove(self.random_number)
        print('\n\tВыпало число {}!'.format(self.random_number), end=' ')
        print('Осталось номеров:', len(self.lotto))

    def start(self):
        while self.comp_number_matches != 15 and self.player_number_matches != 15:
            self.show_new_number()
            Game().show_card(self.player_card, 'Your')
            Game().show_card(self.comp_card, 'Comp')

            if self.random_number in self.comp_card:
                self.comp_card[self.comp_card.index(self.random_number)] = '--'
                print('\n\tКомпьютер зачеркнул число:', self.random_number)
                self.comp_number_matches += 1

            user_answer = input('\n\tЗачеркнуть выпавшее число? Yes(y)/No(n))')

            if user_answer.lower() == 'y' and self.random_number in self.player_card:
                self.player_card[self.player_card.index(self.random_number)] = '--'
                print('\nВы зачеркнули число:', self.random_number)
                self.player_number_matches += 1
            elif user_answer.lower() == 'y' and self.random_number not in self.player_card:
                print('Нельзя зачеркивать числа, которых нет в карточке. Вы проиграли!')
                return
            elif user_answer.lower() == 'n' and self.random_number in self.player_card:
                print('Если число есть в карточке, нужно его зачеркнуть. Вы проиграли!')
                return
            elif user_answer.lower() == 'n' and self.random_number not in self.player_card:
                pass
            else:
                print('Нужно вводить "y" или "n". Вы проиграли!')
                return

    def finish(self):
        if self.comp_number_matches == 15:
            print('Победил компьютер!')
        elif self.comp_number_matches == 15 and self.player_number_matches == 15:
            print('Ничья!')
        elif self.player_number_matches == 15:
            print('ПОЗДРАВЛЯЕМ! Вы победили!')


play = Play()
play.start()
play.finish()
