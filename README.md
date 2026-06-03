Futballisták piaci értékének többváltozós regressziós modellel történő elemzése

A projekt célja: 

A projekt célja a profi labdarúgók piaci értékét befolyásoló fundamentális tényezők vizsgálata egy keresztmetszeti adatbázison. A kutatás arra keresi a választ, hogy a játékosok életkora, pályán töltött ideje, szerződésük hossza, nemzetisége, posztja, gólhozzájárulásuk, és az, hogy milyen ligában játszanak milyen mértékben és milyen áttételeken keresztül határozzák meg a becsült piaci árukat.

Adatforrás: 

Az elemzés a Transfermarkt 2025/26-os szezonra vonatkozó hivatalos adatbázisán alapul, amely a Kaggle platformjáról származik. Az adattisztítás során a projekt összekapcsolta a játékosok alapadatait (players.csv), piaci értékeléseit (player_valuations.csv), pályára lépéseit (appearances.csv) és klubadatait (clubs.csv).

Alkalmazott módszertan: 
Az adatelemzés Python (Pandas, NumPy, Statsmodels, Seaborn) környezetben készült, az alábbi lépésekkel:
Adat-előkészítés és Tisztítás: Hiányzó értékek kezelése, outlierek azonosítása, valamint kategorikus változók (posztok, bajnokságok, nemzetiségek) dummy változókká alakítása.
Multikollinearitás Vizsgálata: VIF (Variance Inflation Factor) mutatók számítása és inverz korrelációs mátrix generálása a magyarázó változók lineáris függetlenségének bizonyítására.
Gauss-Markov Feltételek Ellenőrzése: A klasszikus lineáris regresszió feltételeinek vizuális és elméleti tesztelése.
Útelemzés: A magyarázó változók (Életkor és Játékidő) teljes, közvetlen és közvetett hatásainak matematikai szétbontása és vizualizációja.

Főbb eredmények:
1. A modell magyarázóereje: A felépített OLS regressziós modell Rnégyzet értéke 0.401. Ez azt jelenti, hogy a bevont fundamentális változók (életkor, percek, gólok, szerződés hossza, posztok, ligák,nemzetiségek) a játékosok piaci értékében tapasztalható különbségek több mint 40%-át képesek megmagyarázni.
2. parciális hatások: 
Gólhozzájárulás (Goal_Contributions = 0.9883): Ha két, minden más tekintetben (életkor, poszt, bajnokság, játékperc) teljesen megegyező játékost hasonlítunk össze, egyetlen extra gól vagy gólpassz átlagosan közel 1 millió euróval (0.988 M EUR) növeli a játékos piaci értékét.
Szerződés hossza (Contract_Years_Left = 1.7841): Minden egyes hátramaradó év a játékos szerződéséből átlagosan 1.78 millió eurós prémiumot jelent az árában,minden más változatlansága mellett ami a klubok tárgyalási pozíciójának erősödését tükrözi.
Életkor (Age = -0.4228): A teljes modellt tekintve a játékosok minden egyes betöltött életévvel átlagosan 422 ezer eurót veszítenek a piaci értékükből, minden más változatlansága esetén.
3. Útelemzés:
Az útelemzés rávilágított a játékidő és az életkor közötti komplex kapcsolatra a piaci érték meghatározásában:
Életkor: Az életkor teljes hatása negatív (-0.65 M EUR / év). Ugyanakkor a kor előrehaladtával a játékosok jellemzően több játékpercet kapnak (rutin), ami egy enyhe pozitív közvetett hatást (+0.13 M EUR / év) generál, tompítva ezzel a közvetlen értékcsökkenést.
Játékidő: A pályán töltött percek direkt módon növelik az árat (+0.0066 M EUR / perc), igazolva, hogy a stabil játéklehetőség önmagában is értéknövelő tényező.
