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

| Piece | Abbr | Betza    | Promote | Notes |
| ----- | ---- | -------- | ------- | ----- |
| 鷲    | CE   | fbRfB3K  |         |       |
| 狐    | TF   | fbWFfbDA |         |       |
| 鷹    | FF   | fWB      | 鶏      |       |
| 兎    | RR   | fRFbW    | 狐      |       |
| 狼    | VW   | WfF      | 熊      |       |
| 鹿    | VS   | FfW      | 猪      |       |
| 犬    | BD   | fFrlbW   | 狼      |       |
| 猿    | CM   | fFfbW    | 鹿      |       |
| 鳫    | FG   | fFfbW    | 羽      |       |
| 鶏    | FC   | fFrlW    | 延      |       |
| 羽    | SW   | WrlR     | 行      | 1     |
| 烏    | SC   | fWbF     | 鷹      |       |
| 鴟    | SO   | fWbF     | 鷲      |       |
| 風    | LH   | fRbR2    | 天      |       |
| 車    | OC   | fR       | 牛      |       |

1. Wikipedia uses 燕 instead but this piece is different in Tori shogi

## Promoted pieces

| Piece | Betza  |
| ----- | ------ |
| 熊    | K      | 
| 猪    | FfrlW  |
| 延    | fbRWfF |
| 行    | R      |
| 天    | fbN    |
| 牛    | K      |


# Tori shogi

* Size: 7x7
* Promotion zone: 2 farthest ranks

Uses the following pieces from shogi: 王 (as 鵬)

## Extra initial pieces

| Piece | Abbr | Betza    | Promote | Notes |
| ----- | ---- | -------- | ------- | ----- |
| 象    | F    | FfrlW    | 鵰      | 1     |
| 鶴    | C    | FfbW     |         |       |
| 雉    | P    | fDbF     |         |       |
| 左    | L    | fRbrBblF |         | 2     |
| 右    | R    | fRblBbrF |         | 2     |
| 燕    | S    | fW       | 鴈      | 3, 4  |

1. This piece promotes differently in Chu shogi. Unfortunately I couldn't use
鷹 (different piece in Wa shogi)
2. Wikipedia uses 鶉 for both but this is confusing
3. Only two per column
4. Cannot be dropped to give mate

## Promoted pieces

| Piece | Betza    |
| ----- | -------- |
| 鵰    | fBbRWbB2 |
| 鴈    | fAbD     |


# Okisaki shogi

* Size: 10x10
* Promotion zone: 3 farthest ranks

Uses the following pieces from shogi: 王, 飛, 角, 金, 銀, 歩

## Extra initial pieces

| Piece | Abbr | Betza    | Promote | Notes |
| ----- | ---- | -------- | ------- | ----- |
| 妃    | Q    | Q        |         |       |
| 跳    | N    | N        | 今      |       |
| 反    | A    | fbR      | 仝      | 1     |

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

[Forsyth-Edwards notation for shogi](http://shogi.typepad.jp/brainstorm/2007/01/post_11a0.html)
can be used. Non-standard pieces will be enclosed by angle bracket characters.
For instance:
* \<RR>: sente's 兎 (RR) from Wa shogi
* \<bd>: gote's 犬 (BD) from Wa shogi
* \<R>: sente's 右 (R) from Tori shogi
* \<n>: gote's 跳 (N) from Okisaki shogi

## PGN notation

[Western notation](https://en.wikipedia.org/wiki/Shogi#Notation) can be used,
with non-standard pieces enclosed by angle bracket characters. For instance,
given the following starting position (BOD format):

    後手の持駒：
    ９ ８ ７ ６ ５ ４ ３ ２ １
    +---------------------------+
    |v香v桂v銀v金v桂v金v跳v王v香|一
    | ・v飛 ・ ・ ・ ・ ・v角 ・|二
    |v歩v歩v歩v歩v歩v歩v歩v歩v歩|三
    | ・ ・ ・ ・ ・ ・ ・ ・ ・|四
    | ・ ・ ・ ・ ・ ・ ・ ・ ・|五
    | ・ ・ ・ ・ ・ ・ ・ ・ ・|六
    | 歩 歩 歩 歩 歩 歩 歩 歩 歩|七
    | ・ 角 ・ ・ ・ ・ ・ 飛 ・|八
    | 香 玉 跳 金 桂 金 銀 桂 香|九
    +---------------------------+
    先手の持駒：

The game could proceed like this:

    [Variant "kashogi"]
    [FEN "lnsgng<n>kl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LK<N>GNGSNL b - 1"]
    [...]

    1. P-7f P-3d 2. P-6f <N>-5b [...]
