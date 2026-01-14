import { z } from "zod";

//
//   Category
//

export const CategorySchema = z.object({
  id: z.string(),
  name: z.string(),
  level: z.number(),
  parent_ids: z.array(z.string()),
});

export type Category = z.infer<typeof CategorySchema>;

//
//   Category state
//

export const CategoryStateSchema = z.enum(["disabled", "selected", "normal"]);

export type CategoryState = z.infer<typeof CategoryStateSchema>;