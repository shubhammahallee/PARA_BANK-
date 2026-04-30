class TestRegister:

    # ── Valid Data ──────────────────────────
    valid_firstname = "John"
    valid_lastname  = "Cena"
    valid_address   = "Dhankawadi"
    valid_city      = "Pune"
    valid_state     = "Maharashtra"
    valid_zipcode   = "411041"
    valid_phone     = "9876543210"
    valid_ssn       = "SSN123"
    valid_username  = "johncena01"
    valid_password  = "demo"

    # ── Invalid Data ────────────────────────
    empty_firstname = ""
    empty_username  = ""

    # ── Expected Results ────────────────────
    expected_title   = "Welcome"
    error_user_taken = "This username already exists"
