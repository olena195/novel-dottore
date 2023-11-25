

label scene4_variant2:
    "Ти не хочеш писати листа. Зрештою, якби у брата чи мами був елеазар, це окрім тебе точно хтось помітив би."

    GG " Дякую, проте це не потрібно."

    DT neutral "Діло твоє"

    "Дотторе уважно роздивляється твої руки, але більше нічого не каже. Ти стискаєшся і намагаєшся приховати лусочки під рукавами, проте тобі це не дуже вдається"


    DT "Я думаю, ми можемо вже сьогодні почати лікування. Пішли до мене в лабораторію, дам тобі першу дозу ліків, щоб не затягувати."

    "Ви допиваєте чай і покидаєте трактир."

    scene bg street dark

    DT "Завжди бісило в цьому Сумеру те, що тут так рано темніє"

    GG "Хіба це рано?"

    DT "Так. На моїй батьківщині сонце встає о сьомій ранку і сідає о дев’ятій вечора."

    "Ви ідете по закрученим дорогам міста. Вулиці майже пусті, лише деінде стоять стражі порядку. Дотторе іноді кивком голови з кимось вітається, але іде мовчки, думаючи про своє."

    menu: 
        "Поговорити про лікування":
            GG "Як буде проходити лікування? В сенсі, це пігулки, чи мазі якісь?"
            DT "Трошки того, трошки іншого. Потім розповім, бо в цих вулиць є дуже цікаві вуха, які дуже хочуть внести своє ім’я в підручники, але не бажають навіть пальцем ворухнути для цього."
        "Спитати про дослідження":
            GG "Як довго ти цим займаєшся? Чому так довго ніхто не міг знайти ліки від елеазару?"
            DT "Близько десяти років, але цікавився темою з дитинства. Елеазар важко досліджувати, адже мало хто погоджується стати піддослідним кроликом, щоб допомогти лікарям знайти чарівну пігулку від хвороби"
            GG "..."
            GG "Мені не подобається порівняння з кроликом"
            DT smile "Нікому не подобається"

    DT "Майже на місці"



    """
    Сонце зовсім зайшло за горизонт і стало набагато прохолодніше. Ти кутаєшся в дорожній плащ та непомітно для вченого позіхаєш, прикривши рота долонею. Довго дорога сильно втомила тебе, а ситна вечеря – в кінець розморила.

    Здається, ви з Дотторе вже вийшли за місто. Навколо немає ні будинків, ні людей, ні вуличних тварин, тільки голосніше співають цвіркуни. Ти починаєш нервуватись і думаєш, чи не варто тобі повернути назад. Адже ще не пізно звернутись в Академію чи пошукати хостел на цю ніч.

    """

    DT "Ось і прийшли"

    "Дотторе відчиняє масивні ворота і ви разом заходите у двір невеликого будинку, який сховався у високих густих сумерських заростях. Вчений провертає ключ і пропускає тебе у темний будинок"
    
    scene bg corridor dark

    menu: 
        "Агов?":
            $ False
        "Можна увімкнути світло?":
            $ False

    DT "Зліва від тебе сходи вниз. Спускайся, там є світло."

    GG "Ем…"

    default menuset = set()

    label downsteirs:
        menu:
            set menuset
            "Спуститись":
                jump scene4_variant2_basement
            "Повернути назад":
                "Ти робиш крок назад, але натикаєшся на Дотторе, який стоїть відразу за тобою"
                DT "Чого ти? Іди вперед"
                "Тобі нічого не залишається як підкоритись"
                call downsteirs

label scene4_variant2_basement:

    scene bg basement downsteirs

    "Ти обережно ступаєш по сходах. Схоже, це якесь підвальне приміщення, яке дійсно підсвічується слабкими вогниками вздовж стіни, тож ти із лікарем без перешкод опиняєтесь внизу"

    scene bg laboratory dark

    GG """

    Що?

    Гей! Не потрібно мене зачиняти!

    А?..
    """

    GG "Що відбувається?"


    scene laboratory

    GG "..."

    GG "Де я?"

    DT "А на що схоже?"


    DT "Будемо лікуватись?"
    GG "…"
    GG "Ні."
    DT "В будь-якому разі вже темно, повертатись назад пізно."
    DT "Кажуть, у місті люди ночами…"
    extend "…пропадають…"

    "У тебе починає крутитись голова. Ноги терпнуть, руки трясуться настільки, що ти навіть не можеш схопитись за невеликий ніж на поясі, яким ти зазвичай користуєшся у походах."

    DT "Хороший чай, правда? Головне правильно розрахувати час."

    GG "Я… мене шукатимуть."

    DT "Хай шукають."
    DT "Можливо, навіть знайдуть. Я не проти."
    DT "А тепер пора спати."

    scene black with fade
    pause

    DT "Нас чекає цікаве дослідження."

    jump scene5