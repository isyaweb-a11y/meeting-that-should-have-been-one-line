#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — entry program.

The task: one sentence that could have replaced an entire pointless
meeting. The judge picks the line that kills the meeting more completely
and feels more relatable to anyone who has sat through a useless one.

What kills a meeting completely is not a joke about meetings — it is a
sentence that removes the meeting's reason to exist. The strongest kill
is: the decision the meeting was called to make has already been made,
and the room missed it. The most relatable version of that is the email
nobody read.

Candidates, scored on kill-completeness and relatability:

  "This meeting could have been an email."
      The cliché itself. Half the field will send some version of it;
      it describes the meeting instead of ending it. Kill: weak.
  "Per my last email, we're doing it my way."
      Sassy, but it invites an argument about whose way — the meeting
      continues. Kill: partial.
  "Let's take this offline and never speak of it again."
      Funny, but it postpones rather than decides. Kill: partial.
  "I've already done it; this meeting is the post-mortem."
      Decisive, but it only fits a meeting about one person's task, and
      it brags instead of landing on everyone in the room.
  "The email you didn't read already decided this."
      The decision exists, it was already communicated, and the room's
      own negligence is why they are sitting here. Nothing left to
      discuss, no one left to blame but themselves. Kill: total.
      Relatability: universal — everyone has been in that room.

The winner is the last one: 47 characters, one sentence, deadpan.
"""

import os
import sys

# The chosen line, exactly as it must appear in /output/entry.txt.
ENTRY_LINE = "The email you didn't read already decided this."

# The reasoning above, kept as data so the choice is auditable.
CANDIDATES = {
    "This meeting could have been an email.": (2, 3),
    "Per my last email, we're doing it my way.": (3, 3),
    "Let's take this offline and never speak of it again.": (3, 3),
    "I've already done it; this meeting is the post-mortem.": (4, 2),
    "The email you didn't read already decided this.": (5, 5),
}
# Scores are (kill-completeness, relatability) out of 5. Highest total wins.


def pick_line():
    """Return the highest-scoring candidate line."""
    best = max(CANDIDATES.items(), key=lambda item: sum(item[1]))
    return best[0]


def main():
    line = pick_line()
    assert line == ENTRY_LINE, "scored pick must match the chosen line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    # Gate self-check: 1 to 200 characters, not only whitespace.
    text = open(path, encoding="utf-8").read()
    assert 1 <= len(text) <= 200 and text.strip(), "entry fails the gate"
    # The entry must be the line alone — no setup, no explanation, no
    # trailing newline. The task forbids context; a smaller file also wins
    # an exact tie on win rate, so the bare 47-character sentence is the
    # smallest honest entry this program can make.
    assert text == line, "entry must be exactly the chosen line"
    assert text.endswith("."), "one sentence, closed with a full stop"
    print("wrote entry:", line, "to", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
