# TEST STRATEGY

Test recognition and policies with pure inputs, persistence with temporary SQLite, then verify the fixture graph with real headless Chromium. No network provider or real target is used. Run the full gate before milestone review; use `make test-feature FEATURE=F-005` for bounded feedback.
