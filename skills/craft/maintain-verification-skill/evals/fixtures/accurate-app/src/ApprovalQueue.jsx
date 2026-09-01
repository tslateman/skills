export function ApprovalQueue({ week, onApprove }) {
  return (
    <section>
      <p data-testid="week-status">{week.status}</p>
      <button data-testid="week-approve" onClick={() => onApprove(week.id)}>
        Approve week
      </button>
    </section>
  );
}
