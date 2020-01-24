load harness

@test "array_assign" {
  check 'x := [1, 2, 3]' '{x → [1, 2, 3]}'
}

@test "array_concat" {
  check 'x := [1, 2, 3]; x := x + [4, 5]' '{x → [1, 2, 3, 4, 5]}'
}

@test "array_mult" {
  check 'x := [1, 2, 3]; x := x * 2' '{x → [1, 2, 3, 1, 2, 3]}'
}
