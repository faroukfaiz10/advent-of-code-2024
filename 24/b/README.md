Solved manually:

- Run script to get first wrong bit `i`
- Start from `zi` and replace its inputs
- Expected formula is `zi = (xi XOR yi) XOR ((x{i-1} AND y{i-1}) OR (((x{i-1} XOR y{i-1})) CARRY_OVER(i-2)))`
- No need to go deeper because the gates used in carry over are correct (otherwise `i` wouldn't have been the minimal erroring bit).
- Error is easy to fix manually, find the wrong expression, search for what would have been the correct one, and swap them.
- Re-run the script, new `i` should be higher. After 4 iterations/pairs, the gates should be correct.
