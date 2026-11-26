# The Painfully Honest Out-of-Office

[![competition](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/bbulls013/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/bbulls013/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

An entry for the [make.fun The Painfully Honest Out-of-Office bounty](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b): one out-of-office auto-reply that tells the truth without getting anyone fired.

> Thank you for writing; I am out of office and will not read this until I return, when I will skim it guiltily and reply with the convincing enthusiasm of someone who never left.

The line thanks the sender, admits the message will sit unread until the sender returns, and promises a reply performed with convincing enthusiasm — honest about the absence, the inbox, and the enthusiasm, while staying polite enough for a manager to let it stand.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3, standard library only, no network) writes the single line above to `/output/entry.txt`, falling back to `./output/entry.txt` when `/output` cannot be written. The output is deterministic: the same bytes on every run, well under the 200-character gate.

## Layout

- `main.py` — the entry program; writes `/output/entry.txt`
- `README.md` — this file
- `LICENSE` — MIT
