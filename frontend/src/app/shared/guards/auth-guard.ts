import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from '../../auth/auth.service';
import { map } from 'rxjs';

export const authGuard: CanActivateFn = (route, state) => {
  //
  //   Interfaces
  //
  
  const authService = inject(AuthService);
  const router = inject(Router);

  //
  //   Preparing the observable
  //
  
  return authService.isAuthenticated().pipe(
    map((isAuthenticated) => {
      if (!isAuthenticated) {
        router.navigate(["/auth"]);
        return false;
      }
      
      return true;
    })
  );
};
