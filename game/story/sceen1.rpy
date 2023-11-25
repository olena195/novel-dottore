
define O = Character(name="Охоронець", image="guardian")
define T = Character(name="Трактирник", image="tavernkeeper")

label scene1:
    
    scene bg city entrance

    """
    Ти полегшено зітхаєш і пришвидшуєш крок.
    
    Ну нарешті! Кілька тижнів снів під відкритим небом у компанії хмари комарів, десятки кілометрів не найбезпечнішими ділянками лісу, харчування самими лише ягодами та засушеним м’ясом, і ось ти тут – у місті Сумеру!
    
    Аж не віриться. Ти щипаєш себе за руку і, зойкнувши, розумієш, що все навколо реальне.
    
    Що ж, чудово! Залишилось найпростіше: потрапити у місто, повечеряти та знайти Академію.
    
    А ось і вхід.
    """

    show guardian
    with dissolve

    O "Вітаю! Прошу назвати ваше ім’я та ціль прибуття у місто"

    python:
        player_name = renpy.input("Представитись", length=32)
        player_name = player_name.strip()


    # TODO: Унікальні відповіді для кожного варіанта
    menu:
        "Кажуть, що в Академії знайшли ліки від елеазару. Хочу перевірити їх на собі":
            O "Зрозуміло, [GG]. Спитайте детальніше про це у трактирі, туди стікаються всі новини"
        "Підлікуватись та відпочити у гарному місці":
            O "Зрозуміло, [GG]. Спитайте детальніше про це у трактирі, туди стікаються всі новини"
        "Шукаю одного лікаря, який живе тут":
            O "Зрозуміло, [GG]. Спитайте детальніше про це у трактирі, туди стікаються всі новини"

    O """
    Також маю повідомити, що останнім часом почастішали звернення від родичів мандрівників про щезнення людей. 
    
    Тож якщо випили – ідіть відразу у номер готелю, а не бігайте по незнайомим вуличкам у пошуках пригод.

    Та я впевнений, ніякої проблеми немає.
    """

    GG "..."

    O """
    Сумеру – дуже безпечне місто, а ті мандрівники продовжили шлях і зникли десь у незнайомих для них лісах.
    
    Не турбуйтесь!
    
    Гарного вам перебування!
    """

    GG "Дякую!"

    jump scene2