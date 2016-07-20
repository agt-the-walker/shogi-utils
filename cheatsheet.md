I only list shogi variants with drops, and whose board size doesn't differ too
much from regular shogi, for the reasons described in [this page](README.md).


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
| 鳫    | FG   | fFfbW    | 燕      |       |
| 鶏    | FC   | fFrlW    | 延      |       |
| 燕    | SW   | WrlR     | 行      |       |
| 烏    | SC   | fWbF     | 鷹      |       |
| 鴟    | SO   | fWbF     | 鷲      |       |
| 風    | LH   | fRbR2    | 天      |       |
| 車    | OC   | fR       | 牛      |       |

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
| 猪    | F    | FfrlW    | 鵰      | 1     |
| 鶴    | C    | FfbW     |         |       |
| 雉    | P    | fDbF     |         |       |
| 左    | L    | fRbrBblF |         | 2     |
| 右    | R    | fRblBbrF |         | 2     |
| 燕    | S    | fW       | 鴈      | 3, 4  |

1. Wikipedia uses 鷹 instead but this piece is different in Wa shogi
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
香 or 車 (different pieces in regular and Wa shogi).

## Promoted pieces

| Piece | Betza |
| ----- | ----- |
| 今    | WfF   |
| 仝    | WfF   |


# SFEN notation

[Forsyth-Edwards notation for shogi|http://shogi.typepad.jp/brainstorm/2007/01/post_11a0.html]
can be used. For non-standard pieces:
* \*RR\*: sente's 兎 (RR) in Wa shogi
* \*R\*: sente's 右 (R) in Tori shogi
* \*n\*: gote's 跳 (N) in Okisaki shogi
