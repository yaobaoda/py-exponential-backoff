from backoff import backoff_delay


def test_capped_and_nonnegative():
    for a in range(0, 20):
        d = backoff_delay(a, base_ms=100, cap_ms=5000, rng=lambda: 1.0)
        assert 0 <= d <= 5000
