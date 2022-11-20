import random


class Player:
    def __init__(self, name: str):
        self._name = name

    def __str__(self) -> str:
        return str(self._name)

    def take_candies(self):
        pl_candies = int(
            input(f"Сколько конфет возьмёт игрок {self._name} ? \n"))
        return pl_candies

    def win(self):
        print(print(f"{self._name} Победил"))


class Bot(Player):
    def __init__(self, name: str, *, is_smart=False):
        super().__init__(name)
        self.__is_smart = is_smart

    def take_candies(self, game):
        if game.max_step < game.stack_candies:
            if self.__is_smart: # Умность
                pl_candies = game.stack_candies % (game.max_step+1)
            else: # Не умность
                pl_candies = random.randint(1, game.max_step - 1)
        else:
            pl_candies = game.stack_candies


        print(f"{self._name} взял конфет: {pl_candies}")
        return pl_candies


class Game:
    def __init__(self, _candies, _max_step, *, _mode):
        self.stack_candies = _candies
        self.max_step = _max_step
        self.players = []
        self.mode = _mode  # 0 - игра с игроком; 1 - игра с ботом; 2 - игра с умным ботом

    def add_player(self, player):
        self.players.append(player)
        print(f"Добавлен игрок: {player}")

    def play(self):
        print("Игра началась \n")
        match self.mode:
            case 0:
                for i in range(2):
                    self.add_player(Player(f"Игрок {i+1}"))
            case 1:
                self.add_player(Player("Игрок"))
                self.add_player(Bot("Бот", is_smart=False))
            case 2:
                self.add_player(Player("Игрок"))
                self.add_player(Bot("ГигаБот", is_smart=True))

        random.shuffle(self.players)
        print(f"\nМаксимальное кол-во взятых конфет за ход: {self.max_step}")
        print(f"Конфет сейчас: {self.stack_candies} \n")

        while self.stack_candies > 0:
            for player in self.players:
                if isinstance(player, Bot):
                    pl_candies = player.take_candies(self)
                else:
                    pl_candies = player.take_candies()
                    while pl_candies <= 0 or pl_candies > self.max_step or pl_candies > self.stack_candies:
                        print(
                            f"\nИгрок {player} взял недопустимое кол-во конфет")
                        print(f"Ходит игрок: {player}")
                        print(f"Конфет сейчас: {self.stack_candies} \n")
                        pl_candies = player.take_candies()

                self.stack_candies -= pl_candies
                print(f"Осталось {self.stack_candies} конфет \n")

                if self.stack_candies == 0:
                    player.win()
                    return
