import { UserSchema } from "./user.model";
import { z } from "zod";

export const LoginResponseSchema = z.object({
  access_token: z.string(),
  user: UserSchema,
  token_type: z.string(),
});

export type LoginResponse = z.infer<typeof LoginResponseSchema>;