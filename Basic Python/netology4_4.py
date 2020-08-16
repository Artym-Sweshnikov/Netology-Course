stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
for key, values in stats.items():
    if values == max(stats.values()):
        print(key.capitalize(), '-', values)
