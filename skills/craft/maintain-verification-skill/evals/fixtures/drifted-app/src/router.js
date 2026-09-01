import { BulkVoid } from "./BulkVoid.jsx";
import { InvoiceDetail } from "./InvoiceDetail.jsx";
import { InvoiceList } from "./InvoiceList.jsx";
import { NewInvoice } from "./NewInvoice.jsx";
import { PaymentForm } from "./PaymentForm.jsx";

export const routes = [
  { path: "/invoices", component: InvoiceList },
  { path: "/invoices/new", component: NewInvoice },
  { path: "/invoices/:id", component: InvoiceDetail },
  { path: "/invoices/:id/payment", component: PaymentForm },
  { path: "/invoices/bulk-void", component: BulkVoid },
];
