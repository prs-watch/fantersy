# Fantersy
CLI tool to manage Yahoo! Fantasy Sports.

## Requirement
- Config file as `.yml`.

```yaml
# Yahoo! DN application info.
CLIENT_ID: XXX
CLIENT_SECRET: YYY
FANTASY:
    # select sport from mlb/nba/nhl/nfl
    SPORT_TYP: mlb
    # league id
    LEAGUE_ID: @@@@
```

## Usage

```bash
$ cd /dir/to/fantersy
$ python fantersy/client.py
# --- you have to select config from dialog.
$ authorization code >> ZZZZZ
$ Fantersy >> league
+-------------+--------------+
|    NAME     |   CONTENT    |
+=============+==============+
| LEAGUE NAME |  TEST MLB LG |
+-------------+--------------+
| TEAM NUMBER | 14           |
+-------------+--------------+
| START       | 2018-03-29   |
+-------------+--------------+
| END         | 2018-09-30   |
+-------------+--------------+
$ Fantersy >> roster Marlins
### Marlins ###
+----------+-------------------+------+
|   POS    |       NAME        | TEAM |
+==========+===================+======+
| 1B       | Eric Hosmer       | SD   |
+----------+-------------------+------+
| 1B       | Tyler Austin      | MIN  |
+----------+-------------------+------+
| 1B,LF,CF | Cody Bellinger    | LAD  |
+----------+-------------------+------+
| 2B,SS    | José Peraza       | CIN  |
+----------+-------------------+------+
| 2B,SS    | Paul DeJong       | STL  |
+----------+-------------------+------+
| 3B       | Eugenio Suárez    | CIN  |
+----------+-------------------+------+
| C        | Danny Jansen      | TOR  |
+----------+-------------------+------+
| C        | Mike Zunino       | SEA  |
+----------+-------------------+------+
| CF       | Lorenzo Cain      | MIL  |
+----------+-------------------+------+
| CF,RF    | Odúbel Herrera    | PHI  |
+----------+-------------------+------+
| LF       | Corey Dickerson   | PIT  |
+----------+-------------------+------+
| LF       | Khris Davis       | OAK  |
+----------+-------------------+------+
| RF       | Stephen Piscotty  | OAK  |
+----------+-------------------+------+
| RP       | Drew Steckenrider | MIA  |
+----------+-------------------+------+
| RP       | Kirby Yates       | SD   |
+----------+-------------------+------+
| SP       | Eric Skoglund     | KC   |
+----------+-------------------+------+
| SP       | German Márquez    | COL  |
+----------+-------------------+------+
| SP       | José Berríos      | MIN  |
+----------+-------------------+------+
| SP       | Kyle Gibson       | MIN  |
+----------+-------------------+------+
| SP       | Mike Foltynewicz  | ATL  |
+----------+-------------------+------+
| SP       | Mike Leake        | SEA  |
+----------+-------------------+------+
| SP       | Noah Syndergaard  | NYM  |
+----------+-------------------+------+
| SP       | Ryan Borucki      | TOR  |
+----------+-------------------+------+
| SP       | Sean Reid-Foley   | TOR  |
+----------+-------------------+------+
| SP       | Tyler Anderson    | COL  |
+----------+-------------------+------+
| SP       | Zach Eflin        | PHI  |
+----------+-------------------+------+
| SP,RP    | Brad Keller       | KC   |
+----------+-------------------+------+
| SP,RP    | Daniel Mengden    | OAK  |
+----------+-------------------+------+
| SP,RP    | Dereck Rodríguez  | SF   |
+----------+-------------------+------+
| SP,RP    | Framber Valdez    | HOU  |
+----------+-------------------+------+
$ Fantersy >> player position=SP
+-------+-------------------+------+
|  POS  |       NAME        | TEAM |
+=======+===================+======+
| SP    | Bartolo Colon     | TEX  |
+-------+-------------------+------+
| SP    | CC Sabathia       | NYY  |
+-------+-------------------+------+
| SP    | R.A. Dickey       | ATL  |
+-------+-------------------+------+
| SP,RP | Jerome Williams   | STL  |
+-------+-------------------+------+
| SP    | John Lackey       | CHC  |
+-------+-------------------+------+
| SP    | Adam Wainwright   | STL  |
+-------+-------------------+------+
| SP    | Edwin Jackson     | OAK  |
+-------+-------------------+------+
| SP    | Zack Greinke      | ARI  |
+-------+-------------------+------+
| SP    | Scott Kazmir      | ATL  |
+-------+-------------------+------+
| SP,RP | Gavin Floyd       | TOR  |
+-------+-------------------+------+
| SP    | Brandon McCarthy  | ATL  |
+-------+-------------------+------+
| SP    | Félix Hernández   | SEA  |
+-------+-------------------+------+
| SP,RP | Francisco Liriano | DET  |
+-------+-------------------+------+
| SP    | Cole Hamels       | CHC  |
+-------+-------------------+------+
| SP,RP | Anthony Reyes     | SD   |
+-------+-------------------+------+
| SP    | Ervin Santana     | MIN  |
+-------+-------------------+------+
| SP    | Rich Hill         | LAD  |
+-------+-------------------+------+
| SP    | Justin Verlander  | HOU  |
+-------+-------------------+------+
| SP    | Jason Vargas      | NYM  |
+-------+-------------------+------+
| SP    | Scott Feldman     | CIN  |
+-------+-------------------+------+
| SP    | Edinson Volquez   | TEX  |
+-------+-------------------+------+
| SP,RP | Aníbal Sánchez    | ATL  |
+-------+-------------------+------+
| SP,RP | Jason Hammel      | KC   |
+-------+-------------------+------+
| SP    | Ricky Nolasco     | KC   |
+-------+-------------------+------+
| SP    | James Shields     | CWS  |
+-------+-------------------+------+
```