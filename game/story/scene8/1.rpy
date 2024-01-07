init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move, time, child, add_sizes=True, **properties)

        Shake = renpy.curry(_Shake)
    #

#

label scene8_1:

    call day(_("День 5"))
    
    scene bg laboratory
    show dottore
    with dissolve

    DT "Теорія виявилась невірною. Він знову з’являється."
    """
    Дотторе з прикрістю розглядає нові лусочки елеазара, які почали проростати на покритих твердою кірочкою поверхнях рук та ніг.
    
    Ти тамуєш подих і дивишся за кожним його рухом. Звільнені від бинтів кінцівки болять і печуть, але ти боїшся видати хоча б звук.
    """
    DT """
    Як же так…
    
    Зараз не можу це перевірити, але мені здається, що вони стали ще більш грубими, ніж до операції. Як гадаєш?
    """
    GG "…"
    DT """
    
    Конструктивно.
    
    Добре, потрібно продовжувати роботу. Сподіваюсь, тобі сьогодні добре спалось, бо для подальшого лікування обов’язково потрібно, щоб пацієнт почував себе нормально і був у доброму гуморі.
    
    Крім того, наступний етап займе у нас набагато більше часу, тому можемо сьогодні пропрацювати до ночі. Зважай на це.
    """
    GG "…"
    GG "Чому?"
    DT "Тому що операція – це складно. До того ж я ні разу нічого подібного ще не робив"
    GG "Ем… Яка ще операція?"

    window hide
    with None
    show half_black 
    show instruments
    with dissolve

    """
    Дотторе починає викладати поруч із собою на столик медичні інструменти. 
    
    Ти спостерігаєш, як він дістає довгі металеві пінцети, шприци великого об’єму, якісь темні нитки, намотані на котушку, щось схоже на клаптики тканини, колби з рідинами та закручені на кінцях голки.
    """

    hide instruments 
    hide half_black
    with dissolve

    window auto

    DT """
    Знаєш, що цікаво? Я багато часу провів за дослідженням елеазару і зрозумів, що досі нема жодного зафіксованого випадку зараження ним тваринами та птахами.
    
    Чому люди ним заражаються, а тварини – ні? Від чого це залежить?
    
    Я вже пробував переливати кров від тварини пацієнту, але той щось дуже швидко помер. Не знаю, це сталось через кров собаки в його судинах чи тому що він після цього два дні провів у морозильній камері.
    
    Не впевнений до кінця.
    
    Чи хворіють оті гібриди людей і тварин? Жодного такого не бачив.
    
    Чи можемо ми штучно зробити гібрида? Не знаю, треба експериментувати.
    
    Наразі хочу спробувати пересадити тобі шкіру в’ючного яка і подивитись, чи виросте елеазар на ній.
    
    Як тобі ідея?
    """
    GG "…"
    GG "Ти абсолютно хворий! Відпусти мене!"
    DT "Ні, сонце, хвора тут тільки одна людина - ти. Я ж намагаюсь тебе вилікувати."
    GG "Це теж не подіє! Ні в якому всесвіті твої ідеї не спрацюють!"
    DT "Побачимо. За кілька хвилин починаю, налаштовуйся."
    GG "Я не хочу!"
    DT "Я теж не хочу працювати у свій вихідний, але ж хтось повинен це робити."
    GG "Ні! Це не нормально! Мені боляче!"
    DT "Лікуватись боляче, що ж поробиш."
    GG "Ти не лікар! Лікарі не калічать!"

    "Дотторе лише усміхається і більше не вступає у діалог."

    "Він просякає ганчірку рідиною з якоїсь пляшечки без підпису і відразу прикладає її до оголених ран на нозі"

    GG "Ай!"
    DT "Потерпи, треба розмочити поверхню, щоб шкіра добре прижилась."


    menu:
        "Сіпнутись":
            "Ти сіпаєш ногою з такою силою, що Дотторе здригається від легкого переляку, але роботу не перериває."
            "Лише поглядом ковзає по шкіряним ременям, які утримують тебе."

        "Закричати":
            play sound screem
            pause 3
            DT "Тихо ти. Заважаєш"

    """
    Вчений протирає твої руки і ноги не звертаючи уваги на зойки та коментарі. Частина ран починає сочитися кров’ю, але то і не дивно, зважаючи на те, з якою силою Дотторе відривав бинти від тіла кілька хвилин тому.

    Він обробляє голку спиртом, заправляє нитку та щипцями дістає заготований клаптик шкіри яка з жовтуватої рідини, у якій той плавав весь цей час.

    Ти з власного досвіду знаєш, що шкіра яка досить груба, адже у природі їй потрібно витримувати напади хижаків. Навряд вона приживеться, та і чи можливо це взагалі?

    """


    "Дотторе притискає клапоть шкіри до твоєї гомілки і робить перший укол голкою."

    show bg laboratory at Shake((0, 0, 0, 0), 30.0, dist=4)
    show dottore smile 3 at Shake((0, 0, 0, 0), 30.0, dist=3)



    

    GG "Ай! Боляче!"
    DT "Угу. Терпи."
    """
    Голка погано входить у тканини, застрягаючи в твоєму тілі.
    
    Біль просто пекельний.
    """

    menu:
        "Закричати":
            play sound screem

    scene bg black
    show hands operation
    with dissolve

    "Нитка безкінечно довго тягнеться крізь м’язи та нерви, пронизує судини"

    "Перший кривий стібок зроблений."

    "Другий кривий стібок знову починається з болючого укусу голкою в оголений закривавлений епітелій."

    menu:
        "Закричати":
            play sound screem
            pause 3
            DT "Тихіше ти. Заважаєш"

    """
    Укол голкою.

    Нитка. Довга.
    
    Пінцет.
    
    Вузлик.
    """

    menu:
        "Закричати":
            play sound screem
            pause 3
            DT "Циц!"


    """
    Укол.

    Нитка.

    Пінцет.

    Вузлик.

    Укол…
    """

    scene black with dissolve

    menu:
        "Закричати":
            play sound screem
            pause 5

    jump scene8_1_night


label scene8_1_night:

    scene black

    """
    …
    
    …
    
    …
    """
    
    DT "…операція пройшла успішно…"
    
    "…"
    
    DT "…період реабілітації…"

    menu:
        "Відкрити очі":
            $ False

    "…"

    menu:
        "Відкрити очі":
            $ False

    scene bg laboratory
    show dottore
    with openeyes

    DT "О, хто тут у нас прокинувся!"

    """
    Ти хочеш закрити очі і знову провалитись у ту спокійну тиху темряву, де немає болю та цього безумного вченого у масці.
    
    Руки та ноги болять так сильно, що хочеться відділити їх від тіла назавжди.
    """
    
    DT "Поки ти спиш, я встиг поприбирати операційну, повечеряти та написати звіт. Як ти себе почуваєш?"

    menu:
        "Краще не буває":
            $ False
        "Болить":
            $ False
        "Дуже погано":
            $ False

    DT "Так і запишу. Голова не крутиться? Нудить? Хочеш пити? Їсти? Спати?"


    """
    Ти зітхаєш. Якщо чесно – все і одночасно, але говорити нема сил.
    
    Пришита шкіра відчувається чужорідною, огрубілою. Гидко.
    
    Ти хочеш перевернутись на інший бік, щоб не бачити Дотторе, але традиційно пристебнуті кайданками до металевої труби.
    
    Нічого нового.
    """

    DT "Твоя їжа поруч. Завтра прийду перевірити, як ти тут, а поки відпочивай і набирайся сил."

    hide dottore with dissolve

    "Дотторе йде, зачинаючи двері у лабораторію на ключ."

    "Ти сідаєш вище і оглядаєш результат роботи вченого. Жахливо."

    show hands operation after

    """
    Клаптики чужорідної шкіри пришиті досить неакуратно, з-під них постійно сочиться кров та інші рідини.
    
    І біль. Все болить.
    
    Ти зітхаєш. Що робити далі?
    """

    menu: 
        "Поїсти та відпочити":
            $ False
        "Спробувати звільнитись":
            $ tried_to_escape_counter += 1
            """
            Ти сідаєш зручніше і роздивляєшся кайданки, якими Дотторе прикував тебе до труби.
            
            Здається, сьогодні вчений залишив більше вільного простору для руки ніж зазвичай, тому ти намагаєшся обережно вислизнути зі сталевих лещат.
            """

    hide hands operation after with dissolve
    "Ти їси холодний прісний суп, який залишив тобі вчений. Що ж, це краще, ніж нічого."
    "Відставивши тарілку ти вкладаєшся на брудному матраці і провалюєшся у тривожний неглибокий сон."

    jump scene9_1