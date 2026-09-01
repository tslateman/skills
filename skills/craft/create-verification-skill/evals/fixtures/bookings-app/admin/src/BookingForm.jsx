import { useState } from "react";

export default function BookingForm({ onCreated }) {
  const [roomCode, setRoomCode] = useState("");
  const [checkIn, setCheckIn] = useState("");
  const [checkOut, setCheckOut] = useState("");
  const [error, setError] = useState(null);

  async function submit(e) {
    e.preventDefault();
    setError(null);
    const res = await fetch("/api/bookings", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ room_code: roomCode, check_in: checkIn, check_out: checkOut }),
    });
    if (!res.ok) {
      setError("could not create booking");
      return;
    }
    onCreated(await res.json());
  }

  return (
    <form onSubmit={submit} data-testid="booking-form">
      <input aria-label="Room code" value={roomCode} onChange={(e) => setRoomCode(e.target.value)} />
      <input aria-label="Check in" type="date" value={checkIn} onChange={(e) => setCheckIn(e.target.value)} />
      <input aria-label="Check out" type="date" value={checkOut} onChange={(e) => setCheckOut(e.target.value)} />
      <button type="submit">Create booking</button>
      {error && <p role="alert">{error}</p>}
    </form>
  );
}
