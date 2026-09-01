package main

import (
	"encoding/json"
	"log"
	"net/http"
)

type Booking struct {
	ID       string `json:"id"`
	RoomCode string `json:"room_code"`
	CheckIn  string `json:"check_in"`
	CheckOut string `json:"check_out"`
	Status   string `json:"status"`
}

func main() {
	http.HandleFunc("/api/health", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
	})
	http.HandleFunc("/api/bookings", handleBookings)
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handleBookings(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodPost:
		var b Booking
		if err := json.NewDecoder(r.Body).Decode(&b); err != nil {
			http.Error(w, "bad payload", http.StatusBadRequest)
			return
		}
		b.Status = "confirmed"
		w.WriteHeader(http.StatusCreated)
		json.NewEncoder(w).Encode(b)
	case http.MethodGet:
		json.NewEncoder(w).Encode([]Booking{})
	default:
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
	}
}
