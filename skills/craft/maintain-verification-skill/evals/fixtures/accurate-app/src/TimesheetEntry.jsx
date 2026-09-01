export function TimesheetEntry({ onSubmit }) {
  return (
    <form onSubmit={onSubmit}>
      <input aria-label="Hours" name="hours" />
      <button data-testid="hours-submit">Log hours</button>
    </form>
  );
}
