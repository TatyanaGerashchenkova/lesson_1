time = int(input('Введите время в секундах: '))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 60
print(f'{hours:=02}', ':', f'{minutes:=02}', ':', f'{seconds:=02}', sep='')
