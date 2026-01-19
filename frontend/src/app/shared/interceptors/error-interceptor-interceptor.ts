import { HttpInterceptorFn } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { ErrorSchema } from '../models/error';
import { throwError } from 'rxjs';
import { ErrorWrapper } from '../errors/error-wrapper';

export const errorInterceptorInterceptor: HttpInterceptorFn = (req, next) => {
  return next(req).pipe(
    catchError((error) => {
      const e = ErrorSchema.safeParse(error.error.detail);

      if (!e.success) {
        return throwError(() => {
          return new ErrorWrapper(
            "Une erreur est survenue",
            "Une erreur inattendue est survenue",
            error);
        });
      }

      const data = e.data;

      return throwError(() => {
        return new ErrorWrapper(
          data.user_safe_title,
          data.user_safe_description,
          new Error(data.dev));
      });
    })
  );
};
