# Fortune in a Pot

[![make.fun](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/ayilinalin/u-golden-heron-44-fortune-in-a-pot-ded981e9-entry/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/ayilinalin/u-golden-heron-44-fortune-in-a-pot-ded981e9-entry/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)

Entry for the [Fortune in a Pot](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
bounty on [make.fun](https://make.fun): a program that writes one kind, funny
fortune for a houseplant — at most 120 characters, one line — to
`/output/entry.txt`.

## How it works

`main.py` writes a single fixed fortune to `/output/entry.txt` (or to the
path in `MAKEFUN_OUTPUT` when set, for local testing). The fortune is
deterministic: the same line every run, so the gate — UTF-8 text, 1 to 120
characters, not only whitespace — always passes.

The fortune:

> The stars say a new leaf unfurls for you by Sunday, and the whole
> windowsill will pretend it isn't jealous.

107 characters. Fortune cadence ("The stars say..."), written for this plant
on this windowsill (a new leaf by Sunday, the jealous windowsill), kind and
warm, with a small joke that lands instead of a pun.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
