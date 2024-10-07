#ITERABLE: egy objektuim amely képes egyesével visszaadni az elemeit (pl: list, string)
#ITERATOR: egy speciális objektum, amely egyszerre egy elemet ad vissza egy iterable-ből, az iter() function-nel hozzuk létre, és a next() function-t hívjuk meg
#ITERATION: elemenként haladás folyamata, egy elemről a másikra való eljutást nevezzük iterációnak
#LOOP: automatizálja az iteration folyamatát

#PÉLDA:

#ITERABLE: Spotify (vagy bármilyen) zene lejátszási lista
#ITERATOR: Mi magunk, akik egyik zeneszámról a másikra tudunk kattintani a next gombbal (>>). Tudjuk, hogy most melyik szám szól, és képesek vagyunk a következőre ugrani
#ITERATION: a következő számra való ugrás a next gombbal
#LOOP: automatikus lejátszás anélkül, hogy mi magunk megnyomnánk a next gombot, egészen addig amíg van zene a listában

#ITERABLE:
playlist = ["I'm a barbie girl", "8 óra munka", "Autó egy szerpentinen", "Heavy is the crown"]
#ITERATOR:
it = iter(playlist)
print(type(it))
#ITERATION:
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#miért egy jó nekünk egy iterator?
# nem töltődik be az egész collection a memóriába, mindig az aktuális elemet tároljuk (lazy evaluation)
#LOOP ->