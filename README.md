# Exponential backoff with jitter

```
backoff.py
```
Look at the test suite next to the implementation for concrete examples.

Minimal delay calculator. Computes exponential backoff with full jitter using only the standard library. Zero external packages.

A quick gotcha that bit me: if you cap the maximum delay too high, `time.sleep()` can throw an OverflowError on 32-bit systems. Keep your ceiling reasonable.

## Questions people ask

**Is there an SDK I should install first?**  
No. `backoff.py` makes plain HTTP requests. The setup is just `python3` and one environment variable. That is the whole dependency tree.

**How much of this is reusable?**  
Copy `backoff.py`. That is the only logic worth keeping. The surrounding code just exists to make the example run standalone.