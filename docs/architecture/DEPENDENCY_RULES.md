# DEPENDENCY RULES

Core imports no adapters. Policy and recognition depend on core only. Browser imports policy for defense in depth; storage and evidence must not import Playwright. CLI wires dependencies; reporting imports storage, never the explorer. Future models do not receive an executor or an unrestricted URL.
