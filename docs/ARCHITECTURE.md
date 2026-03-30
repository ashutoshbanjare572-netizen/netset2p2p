# Architecture

`netset2p2p` currently has two layers:

- `netset2p2p.converter`: parse netset lines and emit p2p ranges
- `netset2p2p.cli`: argument parsing and file I/O

As parsing rules mature, keep conversion logic independent from CLI behavior so
it remains easy to test and reuse as a library.
