export function InvoiceDetail({ invoice, onSend }) {
  return (
    <section>
      <h1>Invoice {invoice.number}</h1>
      <p data-testid="invoice-status">{invoice.status}</p>
      <button data-testid="invoice-send" onClick={() => onSend(invoice.id)}>
        Send
      </button>
    </section>
  );
}
