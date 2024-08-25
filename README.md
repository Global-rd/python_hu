# Python Kezdőknek

Ez a repository a kezdő Python kurzushoz első stream-jéhez jött létre. Itt érheted el az órákon tanultakat, illetve itt kezeljük a házi feladatokat is.

## Tartalomjegyzék

- [Követelmények](#követelmények)
- [Telepítés](#telepítés)
- [Hozzájárulás-Házi Feladat](#hozzájárulás)
- [Contributing Flow](#contributing-flow)

## Követelmények

- Python 3.10+
- Git

## Telepítés

1. Klónozd a repository-t a gépedre (minden alábbi lépéshez használhatod a Github Desktop-ot is):

    ```bash
    git clone https://github.com/Global-rd/python_hu.git
    ```

2. Lépj be a projekt könyvtárába:

    ```bash
    cd path/to/repo/python_hu
    ```

3. Telepítsd a szükséges csomagokat (ha vannak):

    ```bash
    pip install -r requirements.txt
    ```

## Hozzájárulás-Házi Feladat

A házi feladatok beküldéséhez kövesd a következő flow-t:

### Contributing Flow

1. **Pull-old a változásokat** a main-ből a local repo-dba:

    ```bash
    git pull https://github.com/Global-rd/python_hu.git
    ```

3. **Hozz létre egy új branch-et** a házidhoz:

    ```bash
    git checkout -b uj-branch-nev
    ```

4. **Commit-eld** a változtatásokat:

    ```bash
    git add .
    git commit -m "Rövid leírás a módosításokról"
    ```

5. **Push-old fel** a módosításokat:

    ```bash
    git push origin uj-ag-nev
    ```

6. **Hozz létre egy Pull Request-et** (PR) a GitHub-on.

7. A PR-nek legalább egy review-on kell átmennie. A review során István ellenőrzi a kódodat, visszajelzést kapsz, ezután merge-elheted a `main`-be.

8. A `main` ágra közvetlenül nem lehet commitolni; minden változás csak PR-en keresztül érkezhet.

