Futballisták piaci értékének keresztmetszeti regressziós elemzése
"""

# 1. FÁZIS: Adatbeolvasás, csomagok importálása és adattisztítás
# TODO: pandas, statsmodels, seaborn, matplotlib importálása
# TODO: Nyers Kaggle CSV beolvasása, NA értékek kezelése
# TODO: Kapusok (GK) kiszűrése és az outlierek korai vizualizációja

# 2. FÁZIS: Dummy változók generálása és az elemzési adatbázis felépítése
# TODO: Kvalitatív változók (posztok, ligák) dummyvá alakítása (referenciacsoport kihagyásával)
# TODO: A modellezésre kész, tiszta elemzési mátrix összeállítása

# 3. FÁZIS: OLS Regresszió és Változószelekció (Backward Elimination)
# TODO: Teljes alapmodell futtatása az összes magyarázó változóval
# TODO: Nem szignifikáns változók (p > 0.05) lépésenkénti kidobása, amíg csak szignifikáns változó marad

# 4. FÁZIS: Multikollinearitás, VIF-mutatók és Modellfeltételek vizsgálata
# TODO: VIF mutatók számítása a végleges, szignifikáns modellen
# TODO: A klasszikus 5 lineáris regressziós modellfeltétel (pl. maradékok normalitása) tesztelése

# 5. FÁZIS: Útelemzés (Path Analysis)
# TODO: Közvetett és közvetlen hatások modellezése (pl. Életkor -> Játékidő -> Piaci érték)
