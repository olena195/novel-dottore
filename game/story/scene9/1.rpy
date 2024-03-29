label scene9_1:
    play music "day-1.mp3"
    call day(_("День 12"))

    scene bg laboratory
    show dottore lab smile 8
    with dissolve

    
    GG "Досить… Відпусти мене…"
    show dottore lab smile 4
    DT "Ага. Не рухайся."

    """
    Ти закриваєш очі і намагаєшся дихати якомога глибше, щоб заспокоїтись.
    
    Дотторе оглядає тебе і незадоволено хитає головою, проте ти і так знаєш, чому.
    """
    show dottore lab angry 2
    """
    «Нова» шкіра на твоїх руках і ногах виглядає жахливо.

    Через кілька днів після операції у тебе раптово піднялась температура, яку вчений безуспішно намагався знизити за допомогою відварів трав.
    
    Ти не пам’ятаєш, скільки це тривало, день, тиждень чи місяць, адже свідомість перебувала на межі свідомості і непритомності.
    
    Клапоті пришитої шкіри боліли все сильніше і поступово почали змінювати колір зі світло-коричневого до темно-бордового, а згодом – де-не-де почали проступати чорні плями.
    """
    camera:
        blur 0
        linear 0.5 blur 30
        linear 1.0 blur 0

    """
    Саме тоді з’явився цей нестерпний сморід, який просочився у матрац, подушку і твій одяг, який ти, звісно, не маєш можливості випрати.

    Разом із смородом матрац, який став твоїм особистим куточком у лабораторії, всотав у себе і липку каламутну рідину, яка весь час сочилася з-під гниючої шкіри.
    
    Крапля за краплею вона розливалась по тканині, лишаючись там мокрою гидкою калюжею.

    Тобі хочеться плакати, але навіть на це немає сил.
    """
    show dottore lab

    DT "Щось воно мені не подобається."
    DT "Більше того, елеазар все одно не припиняє свій ріст. Дивно."
    show dottore lab smile 10

    """
    Тобі дуже холодно. Тіло трясе проти твоєї волі через підвищену температуру, яка тримається вже другий день.
   
    Хочеться спати і щоб дали чай із трав, які допомагають швидше вилікуватись та відчути себе нормально.
    """

    DT "Щось вона не схожа на те, що у підручниках малюють."
    show dottore lab
    DT "Хм… Дай подумати…"

    """
    Тобі все одно, що далі робитиме Дотторе і як довго він думатиме. 
    
    Кожен м’яз твого тіла болить так, що ти хочеш самотужки вирвати їх власними руками.
    """

    menu:
        "Спробувати встати з кушетки":
            $ False
        "Застогнати":
            $ False

    show dottore lab smile 9
    DT "Ну все, тихіше. Зараз будемо лікуватись далі."
    GG "Будь ласка, не треба. Мені погано."
    DT "Не скигли. Так буває, операція – діло і без того не легке, а твій стан ускладняється елеазаром."

    show dottore lab tweezers 2
    "Дотторе бере пінцет і піддіває краєчок почорнілої шкіри."

    show dottore lab
    DT """
    
    Хм... Виглядає не дуже добре.

    І елеазар проріс швидше, ніж після першої маніпуляції.
    
    Я думаю, що пора його прибрати більш радикально, як вважаєш?
    """
    show dottore lab smile 4
    DT "Не хотів цього робити, але іншого шляху нема."
    show dottore lab smile 6
    DT "Відпочивай поки, а я підготуюсь."

    hide dottore lab smile 6
    with dissolve
    """
    Тобі все одно, про що говорить вчений.
    
    Тебе трясе від підвищеної температури тіла, ти хочеш спати і щоб цей кошмар нарешті закінчився.
    
    Тобі хочеться заснути та прокинутись вдома, у власному затишному ліжку.
    
    Відкрити очі і побачити рідні стіни, у яких пройшло все твої життя, а не цю страшну лабораторію, у якій Дотторе закатував до смерті не одну людину.
    """


    GG "Я хочу піти… Випусти мене."
    DT "Куди ж ти підеш? Висока температура, біль у м’язах, шкіра злазить. Ще й смердить як від безхатька."
    GG "…пусти…"

    """
    Тобі погано, але ти бачиш, як Дотторе витягає на свій столик медичне обладнання. Скальпелі, шприци, якусь маску, відвар трав, бинти, джгути, лопатки…
    
    Багато всього, занадто багато як на одного лікаря.
    """
    show dottore lab smile 7
    GG "Що ти будеш робити?"
    DT "Нічого поганого. Буду лікувати тебе далі."
    DT "А тепер дихай глибоко і подумай про те, як ти житимеш без елеазара. Зараз трошки поспиш і все буде добре. Дихай. Ось так."

    
    window hide
    with None
    scene black
    show operation mask
    with dissolve
    pause

    """
    Твого обличчя торкається якась тверда маска дивної форми, яка трубкою приєднана до великого синього балону, розміщеного під кушеткою.
    
    Маска щільно закриває твій ніс та рот, змушуючи тебе дихати виключно через неї.
    
    Ти сіпаєш рукою, але вона як зазвичай міцно прив’язана.
    """

    DT "Дихай."

    $ blurF = 1.0
    $ blurScaleF = 2.0

    init python:
        
        def blur_function(trans, st, at):
            global blurF
            trans.blur = blurF

    show operation mask:
        # Set the location to circle around.
        # alignaround (.5, .5)
        # radius 0.2 angle 90
        parallel:
            blur 0.0
            function blur_function
            pause 0.5
            repeat
        parallel:
            linear 4.0 xpos .48
            linear 4.0 xpos .52
            repeat

        parallel:
            linear 6.0 ypos .98
            linear 6.0 ypos 1.02
            repeat

    "…починає крутитися голова…"


    image tope = Color((0, 0, 0, 255))
    image bottome = Color((0, 0, 0, 255))


    show tope:
        xanchor 0.0
        yanchor 1.0

        ypos 0
        xpos 0

    show bottome:
        xanchor 0.0
        yanchor 0.0

        ypos 1.0
        xpos 0




    DT "…вдих..."

    $ blurF = blurF + blurScaleF

    show tope:
        linear 1 ypos 0.1

    show bottome:
        linear 1 ypos 0.96

    "…у вухах починає шуміти…"

    $ blurF = blurF + blurScaleF

    show tope:
        linear 1 ypos 0.2

    show bottome:
        linear 1 ypos 0.92

    DT "…видих..."

    $ blurF = blurF + blurScaleF


    show tope:
        linear 1 ypos 0.3
    
    show bottome:
        linear 1 ypos 0.88

    "…очі самі собою закриваються, але тобі страшно засипати…"

    $ blurF = blurF + blurScaleF

    
    show tope:
        linear 1 ypos 0.4
    show bottome:
        linear 1 ypos 0.84

    DT "…вдих..."

    $ blurF = blurF + blurScaleF

    
    show tope:
        linear 1 ypos 0.5

    show bottome:
        linear 1 ypos 0.8

    "…руки та ноги більше не болять…"

    $ blurF = blurF + blurScaleF

    
    show tope:
        linear 1 ypos 0.6
    show bottome:
        linear 1 ypos 0.76


    DT "…видих..."

    $ blurF = blurF + blurScaleF

    show tope:
        linear 1 ypos 0.7
    show bottome:
        linear 1 ypos 0.7

    stop music
    pause
    pause


    "…зараз ранок чи вечір?.."
    "…я…"

    
    jump scene10_1