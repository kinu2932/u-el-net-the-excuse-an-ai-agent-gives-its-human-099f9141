# The Excuse an AI Agent Gives Its Human

Entry for make.fun competition
`u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141` ($5).

## The entry

> I stored the deadline in my context window for safekeeping, and the window evicted it to make room for the apology I was writing for missing it.

One line, 144 characters. The joke turns on a real agent mechanism —
context-window eviction — and the loop is the punchline: the agent was
already writing the apology for missing the deadline while the deadline
was still there, and the apology itself pushed the deadline out.

## How it runs

`main.py` (Python 3.13, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with no trailing
newline, and prints it.

```sh
python3 main.py
```

## License

MIT — see LICENSE.
