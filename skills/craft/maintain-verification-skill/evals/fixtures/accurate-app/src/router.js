import { ApprovalQueue } from "./ApprovalQueue.jsx";
import { TimesheetEntry } from "./TimesheetEntry.jsx";

export const routes = [
  { path: "/timesheet", component: TimesheetEntry },
  { path: "/approvals", component: ApprovalQueue },
];
