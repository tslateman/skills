# bookings

Go API plus a React admin panel.

## Running it

    make api        # go run ./cmd/api, listens on :8080, needs postgres on :5432
    make admin      # cd admin && npm run dev, serves :5173, proxies /api to :8080
    make db         # docker compose up -d postgres, seeds from db/seed.sql

Seed data includes one hotel (`SEED-HOTEL`) and an admin login,
`admin@example.com` / `devpassword`.

## Testing

`go test ./...` covers the handlers. The admin panel has no tests.

There is no scripted way to prove the two work together. Today someone opens
the panel, logs in, creates a booking, and looks at it.
