| Characteristic | Blocks | Values in the tests |
|---|---|---|
| C1 Value of stars | below 1, 1 to 5 (base), above 5 | 0, 3, 6 |
| C2 Type of stars | whole number (base), decimal, text, missing | 3, 3.5, "3", no field |
| C3 Pizza | exists (base), does not exist | a new pizza, 999999999 |
| C4 Token | the user's own (base), none, wrong length | from auth, no header, token short |


| Block | Test |
|---|---|
| C1 below 1 | `test_stars_out_of_range[0]` |
| C1 1 to 5 (base) | `test_base_choice_is_saved` |
| C1 above 5 | `test_stars_out_of_range[6]` |
| C2 whole number (base) | `test_base_choice_is_saved` |
| C2 decimal | `test_stars_decimal_is_refused` |
| C2 text | `test_stars_text_is_refused` |
| C2 missing | `test_stars_missing_is_refused` |
| C3 exists (base) | `test_base_choice_is_saved` |
| C3 does not exist | `test_unknown_pizza_is_refused` |
| C4 own token (base) | `test_base_choice_is_saved` |
| C4 none | `test_no_token_is_refused` |
| C4 wrong length | `test_short_token_is_refused` |