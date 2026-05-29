Futballisták piaci értékének keresztmetszeti regressziós elemzése
"""

# 1. FÁZIS: Adatbeolvasás, Tisztítás és Vizualizáció
# TODO: CSV beolvasása (Pandas)
# TODO: Hiányzó (NA) értékek és kapusok (GK) kiszűrése
# TODO: Piaci ár (Y) eloszlásának és az outliereknek a vizualizációja (Seaborn)
# TODO: Gyors korrelációs mátrix a durva multikollinearitás korai szűrésére

# 2. FÁZIS: Változók és Dummyk kialakítása
# TODO: Dummy változók létrehozása (ligák, posztok) a referenciacsoport elhagyásával
# TODO: A végleges, modellezésre kész (tiszta) elemzési adatbázis összeállítása

# 3. FÁZIS: OLS Regresszió és Változószelekció
# TODO: A teljes modell (összes magyarázó változó) futtatása klasszikus OLS-sel
# TODO: Backward elimination: nem szignifikáns változók logikus, lépésenkénti eltávolítása

# 4. FÁZIS: Modellfeltételek és VIF (A végleges modellen)
# TODO: VIF (Variance Inflation Factor) mutatók ellenőrzése
# TODO: Klasszikus modellfeltételek (Normalitásvizsgálat a maradékokon) ellenőrzése

# 5. FÁZIS: Útelemzés (Path Analysis)
# TODO: Közvetett és közvetlen hatások vizsgálata (pl. életkor -> játékidő -> piaci érték)
