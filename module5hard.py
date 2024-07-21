class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return str(self.nickname)


class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == str(i) and hash(password) == hash(i.password):
                self.current_user = i
                break
            elif nickname == str(i) and hash(password) != hash(i.password):
                print("Неверный пароль")
                break
            else:
                print("Такого пользователя не существует")
                break
        if nickname and password in self.users:
            self.current_user = (nickname, password)

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        user.nickname = nickname
        user.password = password
        user.age = age
        if not self.users:
            self.users.append(user)
            self.current_user = user
        else:
            for i in self.users:
                if str(user) == str(i):
                    print(f'Пользователь {nickname} уже существует')
                    break
                else:
                    self.users.append(user)
                    self.current_user = user
                    break

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            i_is_exists = False
            for j in self.videos:
                if i.title == j.title:
                    print("Такое видео уже существует")
                    i_is_exists = True
                    break
            if i_is_exists:
                break
            else:
                self.videos.append(i)

    def get_videos(self, search):
        search_list = []
        for i in self.videos:
            lower = str(i.title).lower()
            if search.lower() in lower:
                search_list.append(i.title)
        if not search_list:
            return "По вашему запросу ничего не найдено"
        else:
            return search_list

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in self.videos:
                if i.title == title:
                    if i.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет. Пожалуйста, покиньте страницу")
                    else:
                        while i.time_now < i.duration:
                            print(i.time_now + 1, end=" ")
                            i.time_now += 1
                            from time import sleep
                            sleep(1)
                        print("Конец видео")








ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
a = ur.add(v1, v2)


# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


