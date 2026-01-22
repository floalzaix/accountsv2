import { z } from "zod";

export const TransactionSchema = z.object({
  id: z.string().optional().nullable(),
  event_date: z.coerce.date(),
  motive: z.string(),
  to: z.string(),
  bank_date: z.coerce.date(),
  type: z.string(),
  category1_id: z.string().optional().nullable(),
  category2_id: z.string().optional().nullable(),
  category3_id: z.string().optional().nullable(),
  amount: z.number(),
});

export type Transaction = z.infer<typeof TransactionSchema>;