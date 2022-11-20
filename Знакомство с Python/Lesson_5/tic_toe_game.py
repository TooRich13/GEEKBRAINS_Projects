class Player:

    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol
        self.pos = []

    def __str__(self) -> str:
        return str(self.name)

    def step(self, field):
        pos = int(input(f"Куда сходит игрок:  {self.name} - {self.symbol}?: "))
        while (not 0 <= pos <= 9) or (field[pos] != " "):
            print("Некорректная позиция")
            pos = int(
                input(f"Куда сходит игрок:  {self.name} - {self.symbol}?: "))
        field[pos] = self.symbol
        self.pos.append(pos)

    def win(self):
        print(print(f"{self.name} Победил"))


class Game:

    def __init__(self):
        self.win_comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
            0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        self.step = 0
        self.players = []
        self.field = [" " for i in range(9)]

    def add_player(self, player):
        self.players.append(player)

    def print_field(self):

        for pl in self.players:
            print(f"{pl.name} - {pl.symbol}")

        print("Номера позиций: \n")
        print("0|1|2")
        print("-----")
        print("3|4|5")
        print("-----")
        print("6|7|8")

        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(
            self.field[0], self.field[1], self.field[2]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(
            self.field[3], self.field[4], self.field[5]))
        print('\t_____|_____|_____')

        print("\t     |     |")

        print("\t  {}  |  {}  |  {}".format(
            self.field[6], self.field[7], self.field[8]))
        print("\t     |     |")
        print("\n")

    def check_victiry(self, player):
        if (len(player.pos) >= 3):
            for win_comb in self.win_comb:
                if all(comb in player.pos for comb in win_comb):
                    return True
        return False

    def check_tie(self):
        if self.step == 9:
            return True
        return False

    def play(self):
        print("\tИгра началась \n")

        self.add_player(Player("Игрок 1", "X"))
        self.add_player(Player("Игрок 2", "O"))

        self.print_field()

        while True:
            for pl in self.players:
                pl.step(self.field)
                self.step += 1
                self.print_field()
                if self.check_victiry(pl):
                    pl.win()
                    return
                if self.check_tie():
                    print("Ничья")
                    return
