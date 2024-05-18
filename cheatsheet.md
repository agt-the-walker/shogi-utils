I only list shogi variants with drops, and whose board size doesn't differ too
much from standard shogi, for the reasons described in [this page](README.md).


# Shogi

* Size: 9x9
* Promotion zone: 3 farthest ranks

## Initial pieces

| Piece | Name   | Abbr | Betza | Promote | Notes |
| ----- | ------ | ---- | ----- | ------- | ----- |
| 王(玉)| King   | K    | K     |         | 1     |
| 飛    | Rook   | R    | R     | 龍(竜)  |       |
| 角    | Bishop | B    | B     | 馬      |       |
| 金    | Gold   | G    | WfF   |         |       |
| 銀    | Silver | S    | FfW   | 全      |       |
| 桂    | Knight | N    | ffN   | 圭      |       |
| 香    | Lance  | L    | fR    | 杏      |       |
| 歩    | Pawn   | P    | fW    | と(个)  | 2, 3  |

1. Royal piece
2. Only one per column
3. Cannot be dropped to give mate

## Promoted pieces

| Piece | Name   | Betza |
| ----- | ------ | ----- |
| 龍    | Dragon | FR    |
| 馬    | Horse  | WB    |
| 全    |        | WfF   |
| 圭    |        | WfF   |
| 杏    |        | WfF   |
| と    | Tokin  | WfF   |


# Wa shogi

* Size: 11x11
* Promotion zone: 3 farthest ranks

Uses the following pieces from shogi: 王 (as 靏), 歩

## Extra initial pieces

| Piece | Name             | Abbr | Betza    | Promote | Notes |
| ----- | ---------------- | ---- | -------- | ------- | ----- |
| 鷲    | Cloud Eagle      | CE   | fbRfB3K  |         |       |
| 狐    | Treacherous Fox  | TF   | fbWFfbDA |         |       |
| 鷹    | Flying Falcon    | FF   | fWB      | 執      |       |
| 兎    | Running Rabbit   | RR   | fRFbW    | 狐      |       |
| 狼    | Violent Wolf     | VW   | WfF      | 熊      |       |
| 鹿    | Violent Stag     | VS   | FfW      | 猪      |       |
| 犬    | Blind Dog        | BD   | fFrlbW   | 狼      |       |
| 猿    | Climbing Monkey  | CM   | fFfbW    | 鹿      |       |
| 鳫    | Flying Goose     | FG   | fFfbW    | 羽      |       |
| 鶏    | Flying Cock      | FC   | fFrlW    | 延      |       |
| 羽    | Swallow's Wings  | SW   | WrlR     | 行      | 1     |
| 烏    | Strutting Crow   | SC   | fWbF     | 鷹      |       |
| 鴟    | Swooping Owl     | SO   | fWbF     | 鷲      |       |
| 風    | Liberated Horse  | LH   | fRbR2    | 天      |       |
| 車    | Oxcart           | OC   | fR       | 牛      |       |

1. Wikipedia uses 燕 instead but this piece is different in Tori shogi

## Promoted pieces

| Piece | Name             | Betza  |
| ----- | ---------------- | ------ |
| 執    | Tenacious Falcon | fbRBW  |
| 熊    | Bear's Eyes      | K      |
| 猪    | Roaming Boar     | FfrlW  |
| 延    | Raiding Falcon   | fbRWfF |
| 行    | Gliding Swallow  | R      |
| 天    | Heavenly Horse   | ffbbN  |
| 牛    | Plodding Ox      | K      |


# Tori shogi

* Size: 7x7
* Promotion zone: 2 farthest ranks

Uses the following pieces from shogi: 王 (as 鵬)

## Extra initial pieces

| Piece | Name        | Abbr | Betza    | Promote | Notes |
| ----- | ----------- | ---- | -------- | ------- | ----- |
| 象    | Falcon      | F    | FfrlW    | 鵰      | 1     |
| 鶴    | Crane       | C    | FfbW     |         |       |
| 雉    | Pheasant    | P    | fDbF     |         |       |
| 左    | Left Quail  | L    | fRbrBblF |         | 2     |
| 右    | Right Quail | R    | fRblBbrF |         | 2     |
| 燕    | Swallow     | S    | fW       | 鴈      | 3, 4  |

1. This piece promotes differently in Chu shogi. Unfortunately I couldn't use
鷹 (different piece in Wa shogi)
2. Wikipedia uses 鶉 for both but this is confusing
3. Only two per column
4. Cannot be dropped to give mate

## Promoted pieces

| Piece | Name  | Betza    |
| ----- | ----- | -------- |
| 鵰    | Eagle | fBbRWbB2 |
| 鴈    | Goose | fAbD     |


# Okisaki shogi

* Size: 10x10
* Promotion zone: 3 farthest ranks

Uses the following pieces from shogi: 王, 飛, 角, 金, 銀, 歩

## Extra initial pieces

| Piece | Name            | Abbr | Betza    | Promote | Notes |
| ----- | --------------- | ---- | -------- | ------- | ----- |
| 妃    | Queen           | Q    | Q        |         |       |
| 跳    | FIDE Knight     | N    | N        | 今      |       |
| 反    | Reverse Chariot | A    | fbR      | 仝      | 1     |

1. This piece promotes differently in Chu shogi. Unfortunately I couldn't use
香 or 車 (different pieces in standard and Wa shogi).

## Promoted pieces

| Piece | Betza |
| ----- | ----- |
| 今    | WfF   |
| 仝    | WfF   |


# Implementation details

The following section only applies whenever we mix standard and non-standard
pieces, as suggested in [this page](README.md).

## SFEN notation

[Forsyth-Edwards notation for shogi](https://en.wikipedia.org/wiki/Shogi_notation#SFEN)
can be used. Tori and Okisaki pieces will be followed by a single-quote
character while Wa pieces (2 characters) will be followed by @. For instance:
* `RR@`: sente's 兎 (RR) from Wa shogi
* `+RR@`: sente's promoted 兎 (+RR) from Wa shogi
* `bd@`: gote's 犬 (BD) from Wa shogi
* `R'`: sente's 右 (R) from Tori shogi
* `n'`: gote's 跳 (N) from Okisaki shogi
* `+n'`: gote's promoted 跳 (+N) from Okisaki shogi

## PGN notation (and BOD diagrams)

[Western notation](https://en.wikipedia.org/wiki/Shogi#Notation) can be used,
with Tori and Okisaki pieces followed by a single-quote character, to
distinguish them from standard pieces. For instance, given the following
starting position (BOD format):

    後手の持駒：
      ９ ８ ７ ６ ５ ４ ３ ２ １
    +---------------------------+
    |v香v桂v銀v金v桂v金v跳v王v香|一
    | ・v飛 ・ ・v烏 ・ ・v角 ・|二
    |v歩v歩v歩v歩v歩v歩v歩v歩v歩|三
    | ・ ・ ・ ・ ・ ・ ・ ・ ・|四
    | ・ ・ ・ ・ ・ ・ ・ ・ ・|五
    | ・ ・ ・ ・ ・ ・ ・ ・ ・|六
    | 歩 歩 歩 歩 歩 歩 歩 歩 歩|七
    | ・ 角 ・ ・ 烏 ・ ・ 飛 ・|八
    | 香 玉 跳 金 桂 金 銀 桂 香|九
    +---------------------------+
    先手の持駒：

The game could proceed like this:

    [Variant "kashogi"]
    [FEN "lnsgngn'kl/1r2SC@2b1/ppppppppp/9/9/9/PPPPPPPPP/1B2SC@2R1/LKN'GNGSNL b - 1"]
    [...]

    1. P-7f P-5d 2. P-6f SC-5c 3. P-2f N'-5b [...]

For some Wa shogi pieces, it is necessary to distinguish between the promoted
and the non-promoted version of the piece in BOD diagrams. For instance 鷲 can
be either the unpromoted 鷲 (CE) or the promoted 鴟 (+SO). Therefore I propose
the following notation (␣ being the symbol for a space):
* `␣鷲`: sente's 鷲 (CE)
* `v鷲`: gote's 鷲 (CE)
* `^鷲`: sente's promoted 鴟 (+SO) -- this is new
* `V鷲`: gote's promoted 鴟 (+SO) -- this is new
* `␣鴟`: sente's 鴟 (SO)
* `v鴟`: gote's 鴟 (SO)

## ASCII diagrams

https://github.com/gunyarakun/python-shogi shows an example for standard Shogi
("Show a simple ASCII board"). Since we only have enough space for three
characters per piece (including + for promotions), I propose the following
notation for non-standard pieces:
* `␣RR`: sente's 兎 (RR) from Wa shogi
* `+RR`: sente's promoted 兎 (+RR) from Wa shogi
* `␣bd`: gote's 犬 (BD) from Wa shogi
* `␣R'`: sente's 右 (R) from Tori shogi
* `␣n'`: gote's 跳 (N) from Okisaki shogi
* `+n'`: gote's promoted 跳 (+N) from Okisaki shogi

For instance:

     l  n  s  g  n  g  n' k  l
     .  r  .  .  sc .  .  b  .
     p  p  p  p  p  p  p  p  p
     .  .  .  .  .  .  .  .  .
     .  .  .  .  .  .  .  .  .
     .  .  .  .  .  .  .  .  .
     P  P  P  P  P  P  P  P  P
     .  B  .  .  SC .  .  R  .
     L  K  N' G  N  G  S  N  L
