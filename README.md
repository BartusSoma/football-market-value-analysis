# football-market-value-analysis
Cross-sectional regression model for football player market values.
# Futballisták Piaci Értékének Keresztmetszeti Regressziós Elemzése

## 1. Adatbeolvasás, csomagok importálása és adattisztítás
A projekt a szükséges Python könyvtárak (pandas, statsmodels, seaborn) beöltésével és a kiterjedt Kaggle adatbázis importálásával indul. Az adattisztítás során a hiányzó értékek kezelése után a kapusok (GK) eltávolításra kerülnek, mivel árazási logikájuk eltér a mezőnyjátékosokétól. Seaborn ábrákkal korán kiszűrjük a torzító hatású kiugró értékeket (outliereket).

## 2. Dummy változók generálása és az elemzési adatbázis felépítése
A minőségi változókat (bajnokság, poszt) dummy változókká alakítjuk a lineáris regresszió elvárásainak megfelelően. A dummy-csapda (tökéletes multikollinearitás) elkerülése érdekében egy-egy referenciacsoportot szándékosan kihagyunk a modellből, így létrehozva a végleges elemzési adatbázist.

## 3. OLS Regresszió és Változószelekció (Backward Elimination)
Első lépésben lefuttatjuk a teljes alapmodellt az összes magyarázó változó bevonásával. Ezt követi a Backward elimination eljárás: a p-értékek alapján a nem szignifikáns (p > 0.05) magyarázó változókat iteratív módon, lépésenként eltávolítjuk, amíg egy kizárólag szignifikáns együtthatókkal rendelkező modellt nem kapunk.

## 4. Multikollinearitás, VIF-mutatók és Modellfeltételek vizsgálata
A már kizárólag szignifikáns változókat tartalmazó végleges modellen elvégezzük a szükséges ellenőrzéseket:
* **VIF (Variance Inflation Factor):** Ellenőrizzük a magyarázó változók közötti nemkívánatos lineáris kapcsolatokat.
* **Modellfeltételek:** Teszteljük a klasszikus 5 Gauss-Markov feltételt, különös tekintettel a maradéktagok normalitására és eloszlására.

## 5. Útelemzés (Path Analysis)
Az elemzés zárásaként megvizsgáljuk a változók közötti mélyebb, strukturális összefüggéseket. Feltárjuk a közvetlen hatások mellett a közvetett útvonalakat is, különös tekintettel arra, hogy a játékosok életkora a játékidő változásán keresztül milyen áttételes hatást gyakorol a piaci értékre.
