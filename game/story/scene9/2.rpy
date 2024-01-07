label scene9_2:
    
    scene bg laboratory
    with fade

    """
    
    …
    
    …
    
    Болить.
    
    Як же болить.
    
    Ти відкриваєш очі і дуже важко озираєшся навколо.
    
    Дотторе залишив тобі світло у кімнаті, але воно скоріше заважає знову поринути у небуття, ніж прокинутись після втрати свідомості.
    
    Ти знову лежиш на своєму брудному матраці під стіною, а ліва рука прикута до металевої труби «заради безпеки».
    
    Нічого нового.
    
    Хоча можна було би не метушитись: навряд чи тобі вистачило сил кудись втекти.
    
    Вчений дбайливо загорнув закривавлені та обпечені залізом кінцівки у бинти, але тобі неймовірно хочеться зірвати їх з себе і притиснутись до чогось холодного.
    """

    scene bg black
    show legs
    with fade

    """
    Також ти помічаєш, що на правій руці відсутні два нігті. Коли це сталося – ти не пам’ятаєш, але пластини зняті так акуратно, ніби їх там ніколи і не було.
    
    Дивно. Невже Дотторе теж попрацював над цим?
    """

        
    scene bg laboratory
    with fade

    """
    Ти обережно торкаєшся передніх зубів пересохлим язиком. Очевидно, препарат продовжує діяти, адже зуби хитаються ще сильніше, ніж зранку.
    
    Хоч би взагалі не випали.
    
    Ти обережно сідаєш вище, намагаючись не торкатись бинтами матрацу.
    
    Що робити далі?
    """

    menu:
        "Поїсти та відпочити":
            $ dotore_mad += -10
        "Спробувати звільнитись":
            $ dotore_mad += +10
            "Ти сідаєш зручніше і роздивляєшся кайданки, якими Дотторе прикував тебе до труби. Металева конструкція виглядає міцною та надійною і здається, без ключа їх не відкрити."
            "Ти намагаєшся висковзнути крізь кільце, що схопило тебе за кисть, проте нічого не виходить."

    """
    Ти їси холодний суп, який залишив тобі вчений. Що ж, це краще, ніж нічого.
    
    Відставивши тарілку ти вкладаєшся на брудному матраці і провалюєшся у тривожний неглибокий сон.
    """



    jump scene10_2