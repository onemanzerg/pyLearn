from collections import Counter

txt = open('assets/some.txt', 'r')

#txt = """
#В воскресенье, 31 января, в Кинешме группа задержания Кинешемского отдела Росгвардии по сигналу тревоги выехал в один из сетевых магазинов на улице Щорса. - Работники торгового заведения сообщили, что по камерам видеонаблюдения было выявлено ранее совершенное хищение. Тогда неизвестный гражданин похитил продукты и алкоголь на сумму более 5,5 тысяч рублей. Приметы правонарушителя распространили среди персонала. Спустя два дня одна из работниц увидела, что мужчина вновь пришел в магазин, и нажала кнопку тревожной сигнализации, - сообщили в пресс-службе Росгвардии по Ивановской области.  Правоохранители задержали 34-летнего местного жителя. Как выяснилось позже, мужчина ранее уже привлекался к уголовной ответственности. Росгвардейцы передали задержанного сотрудникам полиции для разбирательства. По факту кражи следственными органами полиции возбуждено уголовно дело по ч.1 ст.158 УК РФ.
#"""

word_list = []

for word in txt.split():
    clear_word = ""
    for letter in word:
        if letter.isalpha():
            clear_word += letter.lower()

    word_list.append(clear_word)

print(Counter(word_list))