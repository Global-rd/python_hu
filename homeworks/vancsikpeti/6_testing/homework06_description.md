
A unit testeknél a következőket vedd figyelembe:

-> Írj legalább 2 fixture-t (2 különböző BankAccount object), amiket a tesztjeidben használsz.

-> Írj legalább egy tesztet ami @pytest.mark.parametrize-t használ annak érdekében, hogy a tesztet több input-ra is lefuttassa 
 (pl: teszteld a deposit() method-ot pontosan 0 és negatív szám inputtal is).

-> Tesztelj edge case-eket (pl: pénz küldése nem BankAccount object-nek).

-> Írj teszteket amik arra irányulnak, hogy a megfelelő Exception raise-elődik- e a megadott input-ra.

Extra: a BankAccount class nincs felkészülve minden lehetséges hibára (non-number inputok, küldhetünk e saját magunknak pénzt stb.). 
Nézd át alaposan a kódot, azonosítsd ezeket a hiányosságokat és implementáld a szükséges változtatásokat a saját mappádban lévő file-ban. Ezután írj teszteket amik ezeknek a kiegészítéseknek a helyességét ellenőrzik.
