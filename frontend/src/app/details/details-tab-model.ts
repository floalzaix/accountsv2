import { z } from 'zod';

export const MonthlyValueSchema = z.object({
  title: z.string(),
  january: z.any(),
  february: z.any(),
  march: z.any(),
  april: z.any(),
  may: z.any(),
  june: z.any(),
  july: z.any(),
  august: z.any(),
  september: z.any(),
  october: z.any(),
  november: z.any(),
  december: z.any(),
  total: z.number().optional().nullable()
});

export type MonthlyValue = z.infer<typeof MonthlyValueSchema>;

export type DetailsTabRow = {
  values: MonthlyValue;
  child_rows?: DetailsTabRow[] | null;
};

const DetailsTabRowSchema = z.lazy(() =>
  z.object({
    values: MonthlyValueSchema,
    child_rows: z.array(DetailsTabRowSchema).optional().nullable(),
  })
) as z.ZodType<DetailsTabRow>;


export const DetailsTabSchema = z.object({
  rows: z.array(DetailsTabRowSchema),
  total_row: MonthlyValueSchema.optional().nullable()
});

export type DetailsTab = z.infer<typeof DetailsTabSchema>;
