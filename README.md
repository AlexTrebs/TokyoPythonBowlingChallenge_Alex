# 10 Pin Bowling Challenge 🏆

This repo is for a coding challenge at the Tokyo Python Meetup: Parse
a 10-pin bowling scorecard.

- **Easy**: Sum total pins knocked down.
- **Challenge**: Full official score with strikes (X), spares (/), opens, and 10th-frame bonuses.

Work in groups, tackle it in an hour, then demo in 2 mins.

Branches:

- `easy`: Code skeleton and tests for total pins.
- `challenge`: Code skeleton and tests for full scoring.

## Quick Rules Refresher

- **Frames**: 10 total.
- **Open**: <10 pins over 2 rolls (e.g., "71" = 7+1=8).
- **Gutter Ball -**: 0 pins (e.g., "6-" = 6+0, also "-" = 0+0).
- **Spare /**: 10 pins over 2 rolls (e.g., "6/" = 6+4).
- **Strike X**: 10 on first roll ("X").
- **Score**: Pins + bonuses (next roll for spare, next two for strike).
- **10^th^ Frame**: Up to 3 rolls if strike/spare.

## Setup

The challenge is packaged using a simple `uv` setup.

If you don't have `uv` then visit
[Astral's uv install page](https://docs.astral.sh/uv/getting-started/installation/)

1. **Clone the repo**:

   ```
   git clone https://github.com/ben05allen/TokyoPythonBowlingChallenge.git
   cd TokyoPythonBowlingChallenge
   ```

2. **Sync project:**

   ```
   uv sync
   ```

## Running Tests

Switch to your branch (`git checkout easy` or `challenge`), implement, then:

```
uv run tests
```

Example test output:

## Example Usage

```python
from score_card import pins_knocked_over

scorecard = "9- X 71 6/ 5- 8/ X 7- 3/ X81"
print(pins_knocked_over(scorecard))  # 98 (easy)

# For hard (in challenge branch):
from bowling import full_score
print(full_score("X "*9 + "XXX"))  # 300 (perfect!)
```

---

_Built for Python 3.10+ • License: MIT._
