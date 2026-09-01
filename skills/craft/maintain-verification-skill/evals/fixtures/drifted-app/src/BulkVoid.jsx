import { useState } from "react";

export function BulkVoid({ invoices, onVoid }) {
  const [selected, setSelected] = useState([]);
  return (
    <section>
      <h1>Bulk void</h1>
      {invoices.map((inv) => (
        <label key={inv.id}>
          <input
            type="checkbox"
            onChange={() => setSelected((s) => [...s, inv.id])}
          />
          {inv.number}
        </label>
      ))}
      <button data-testid="bulk-void-confirm" onClick={() => onVoid(selected)}>
        Void selected
      </button>
    </section>
  );
}
