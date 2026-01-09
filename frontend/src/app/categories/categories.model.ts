import { z } from "zod";

export const CategorySchema = z.object({
  id: z.string(),
  name: z.string(),
  level: z.number(),
  parent_ids: z.array(z.string()),
});

export type Category = z.infer<typeof CategorySchema>;