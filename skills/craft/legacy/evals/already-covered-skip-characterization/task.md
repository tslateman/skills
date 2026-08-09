# Task: add stacking limits to coupons

Coupons currently redeem one at a time. Product wants a per-coupon `max_stack` rule: a coupon may combine with at most that many others on one order.

Add the rule to `coupon.py`.

## Expected behaviour

- A coupon declaring `max_stack` refuses to redeem when the order already carries more than that many other coupons.
- Every existing redemption rule keeps working.
