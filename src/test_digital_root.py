"""Test digital_root function."""


test.assert_equals( digital_root(16), 7 )
test.assert_equals( digital_root(195), 6 )
test.assert_equals( digital_root(992), 2 )
test.assert_equals( digital_root(999999999999), 9 )
test.assert_equals( digital_root(167346), 9 )
test.assert_equals( digital_root(0), 0 )