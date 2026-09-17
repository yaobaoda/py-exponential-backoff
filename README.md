# Exponential backoff with jitter

```
backoff.py
```
Run the Python test suite next to the core logic. It shows the exact delay calculations.

Minimal delay calculator. Applies full jitter.

Uses only the Python standard library. No packages to install.

One gotcha that bit me early on: always cap your `max_delay`. If you forget to bound the exponential growth, a long network partition will make your retry loop wait for days.

## Common questions

**Do I need an SDK?**  
No. `backoff.py` sends the request over plain HTTP. The setup is just `python3` and one environment variable. That is the entire dependency tree.