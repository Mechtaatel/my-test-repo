class RatingManager:

  def __init__(self, file_path):
    self.file_path = file_path
    self.data = {}

  def read_data(self):
    # Открываем файл для чтения
    with open(self.file_path,'r') as file:
      data = file.read()

    # Разбиваем строки на отдельные строки
    lines = data.split('\n')

    for line in lines:
      # Разделяем строку на имя и число, разделяя их по двоеточию (' = ')
      parts = line.split(' = ')
      if len(parts) == 2:
        name = parts[0].strip()
        number = int(parts[1].strip())
        self.data[name] = number

  def update_rating(self, name, rating):
    # Обновляем или добавляем нового пользователя в словарь данных
    self.data[name] = rating

  def write_data(self):
    # Открываем файл для записи и записываем обновленные данные
    with open(self.file_path, 'w') as file:
      for name, rating in self.data.items():
        file.write(f"{name}: {rating}\n")


  def sort_and_write_data(self):
    # Сортируем данные по убыванию чисел (рейтингов)
    sorted_data = sorted(self.data.items(), key=lambda x: x[1], reverse=True)

    # Открываем файл для записи
    with open(self.file_path, 'w') as file:
        for name, rating in sorted_data:
            # Записываем данные в формате "имя: рейтинг"
            file.write(f"'{name}' = {rating}\n")




# Пример использования класса
#file_path = 'Raiting.txt'
#rating_manager = RatingManager(file_path)
#rating_manager.read_data()

# Обновление рейтинга или добавление нового пользователя
#rating_manager.update_rating("Новый Пользователь", 777)

# Запись обновленных данных
#rating_manager.write_data()

# Вызываем метод для сортировки и записи данных
#rating_manager.sort_and_write_data()