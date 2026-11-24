# EXPLORATION RULES

Visit new logical states in FIFO order. Per-state actions follow DOM order; each candidate is considered once, with no automatic retry of an uncertain action. Reconstruct a path only through previously allowed fixture interactions, and confirm identity before expanding. Bound depth, state count, action attempts, browser interactions, duration and screenshot bytes.
