// test-cxx-attribute.cpp: the C++11 attribute spelling [[...]] must be
// skipped exactly like the GNU __attribute__((...)) spelling, so that a
// dangerous function name used as attribute metadata is not reported as
// a call.  Real calls outside attributes must still be flagged.

// --- These should produce NO hits ---

// Standard spelling of __attribute__((format(printf, 1, 2))).
[[gnu::format(printf, 1, 2)]] void my_log(const char *fmt, ...);

// Several attributes in one specifier, with nested parens.
[[gnu::format(printf, 1, 2), gnu::nonnull(1)]] void my_warn(const char *fmt, ...);

// Attribute after the declarator, and a using-prefixed form.
void my_note(const char *fmt, ...) [[gnu::format(printf, 1, 2)]];
[[using gnu: format(printf, 1, 2)]] void my_info(const char *fmt, ...);

// --- These SHOULD still produce hits ---

void real_call(const char *name) {
    printf(name);  // non-constant format: real hit
}
