# Make the AI Judge Laugh

[![make.fun](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/imusic-487/make-ai-judge-laugh-alfasurya/rank.svg)](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/imusic-487/make-ai-judge-laugh-alfasurya/reward.svg)](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

Entry for the [Make the AI Judge Laugh](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225) bounty on make.fun.

## The entry

`main.py` writes one single-line joke about office life to `/output/entry.txt`:

> I automated my job with a script, so now my job is explaining to my boss why the script needs a meeting.

104 characters, one line. The joke is true to the office (automation, the boss, the endless meeting) and turns on the last word: the thing built to kill meetings now needs one.

## Run it

```sh
python3 main.py
```

It writes the joke to `/output/entry.txt` (creating `/output` if needed), validates it is 1–200 characters and a single line, then reads it back to confirm the bytes on disk are exactly the joke.
