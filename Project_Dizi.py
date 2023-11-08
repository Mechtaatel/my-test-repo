import pickle
from enum import Enum


class TypeGame(Enum):
  OneVsOne = 1
  TwoVsTwo = 2
  FourVsFour = 3
  Exit = 4


class Math:

  @staticmethod
  def elo_rating(A, B, S_a, S_b):
    Q_a = 10**(A / 400)
    Q_b = 10**(B / 400)
    E_a = Q_a / (Q_a + Q_b)
    E_b = Q_b / (Q_a + Q_b)

    if A <= 2100:
      K_a = 32
    elif A <= 2400:
      K_a = 24
    else:
      K_a = 16

    if B <= 2100:
      K_b = 32
    elif B <= 2400:
      K_b = 24
    else:
      K_b = 16

    if S_a + S_b == 1:
      R_a = A + K_a * (S_a - E_a)
      R_b = B + K_b * (S_b - E_b)
      if R_a < 100:
        R_a = 100
      if R_b < 100:
        R_b = 100
      return R_a, R_b
    else:
      return None


  def OneVsOne():
    A = float(input('Рейтинг игрока A:'))
    B = float(input('Рейтинг игрока B:'))
    S_a = float(input('Player A:'))
    S_b = float(input('Player B:'))

    result = Math.elo_rating(A, B, S_a, S_b)
    if result:
      print('New рейтинг игрока A:', int(result[0]))
      print('New рейтинг игрока B:', int(result[1]))
    else:
      print('Ошибка, вы ввели неправильное значение')


  def TwoVsTwo():
    A1 = float(input('Рейтинг игрока A1:'))
    B1 = float(input('Рейтинг игрока B1:'))
    A2 = float(input('Рейтинг игрока A2:'))
    B2 = float(input('Рейтинг игрока B2:'))
    S_a = float(input('Player A1:'))
    S_b = float(input('Player B1:'))
    #Остальной код


  def FourVsFour():
    A1 = float(input('Рейтинг игрока A1:'))
    B1 = float(input('Рейтинг игрока B1:'))
    A2 = float(input('Рейтинг игрока A2:'))
    B2 = float(input('Рейтинг игрока B2:'))
    A3 = float(input('Рейтинг игрока A3:'))
    B3 = float(input('Рейтинг игрока B3:'))
    A4 = float(input('Рейтинг игрока A4:'))
    B4 = float(input('Рейтинг игрока B4:'))
    S_a = float(input('Player A1:'))
    S_b = float(input('Player B1:'))
    #Остальной код


  def Work():
    print('Выберите тип игры:')
    print(f"{TypeGame.OneVsOne.value} = Один на один")
    print(f"{TypeGame.TwoVsTwo.value} = Два на два")
    print(f"{TypeGame.FourVsFour.value} = Четыре на четыре")
    print(f"{TypeGame.Exit.value} = Выход")

    i = int(input('Ваш выбор:'))

    if i == TypeGame.OneVsOne.value:
      Math.OneVsOne()
    elif i == TypeGame.TwoVsTwo.value:
      Math.TwoVsTwo()
    elif i == TypeGame.FourVsFour.value:
      Math.FourVsFour()
    elif i == TypeGame.Exit.value:
      print('Конец')
    else:
      print('Неправильный выбор')


if __name__ == "__main__":
  Math.Work()
