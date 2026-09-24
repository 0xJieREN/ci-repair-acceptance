# ci-repair acceptance fixture

Disposable, low-privilege target for a live end-to-end acceptance run of
[ci-repair](https://github.com/0xJieREN/ci-repair). Bugs are introduced on
purpose. Workflows have read-only permissions and use no secrets.

The helpers in `calc/` are covered by one workflow job each.
