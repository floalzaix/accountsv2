import { inject, Injectable } from '@angular/core';
import { AsyncHttpClient } from '../shared/services/async-http-client';
import { User } from './user.model';
import { ValidationError } from '../shared/errors/validation-error';
import { ErrorWrapper } from '../shared/errors/error-wrapper';
import { BehaviorSubject, catchError, map, Observable, of, switchMap } from 'rxjs';
import { LoginResponse, LoginResponseSchema } from './login-response.model';
import { Router } from '@angular/router';
import { toSignal } from '@angular/core/rxjs-interop';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  //
  //   Interfaces
  //
  
  private readonly asyncHttpClient = inject(AsyncHttpClient);
  private readonly router = inject(Router);

  //
  //   Methods
  //

  public register(
    { email, password, confirmPassword, pseudo }: {
      email: string;
      password: string;
      confirmPassword: string;
      pseudo: string;
    }
  ): Observable<User> {
    //
    //   Validating the data
    //

    if (password !== confirmPassword) {
      throw new ErrorWrapper(
        "Erreur",
        "Les mots de passe ne correspondent pas",
        new ValidationError("Passwords do not match")
      );
    }

    //
    //   Preparing the observable
    //
    const observable = this.asyncHttpClient.post<User>({
      endpoint: "/auth/register",
      json: {
        email,
        password,
        pseudo,
      },
    });

    return observable;
  }

  /**
   * Logs in a user.
   * 
   * Then stores the given token into the local storage.
   * 
   * @param email - The email of the user.
   * @param password - The password of the user.
   * @returns An observable of the user.
   */
  public login(
    { email, password }: {
      email: string;
      password: string;
    }
  ): Observable<User> {
    
    //
    //   Preparing the observable
    //
    const observable = this.asyncHttpClient.post<LoginResponse>({
      endpoint: "/auth/login",
      json: {
        email,
        password,
      },
    }).pipe(
      map((response) => {
        const loginResponse = LoginResponseSchema.parse(response);
        const user = loginResponse.user;

        localStorage.setItem('access_token', loginResponse.access_token);
        localStorage.setItem('user', JSON.stringify(user));

        this.refresh();

        return user;
      })
    );

    return observable;
  }

  public getUser(): User {
    const user = localStorage.getItem('user');

    if (!user) {
      this.logout();
      this.router.navigate(['/login']);
    }

    return JSON.parse(user as string);
  }

  public isAuthenticated(): Observable<boolean> {
    const token = localStorage.getItem('access_token');
    const user = localStorage.getItem('user');

    if (!token || !user) {
      return of(false);
    }

    const observable = this.asyncHttpClient.get<User>("/auth/me").pipe(
      map(() => {
        return true;
      }),
      catchError(() => {
        return of(false);
      })
    );

    return observable;
  }

  public logout(): void {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
    this.refresh();
    this.router.navigate(['/auth']);
  }

  //
  //   Refreshable signals
  //
  
  private readonly refreshTrigger = new BehaviorSubject<void>(undefined);

  public refresh(): void {
    this.refreshTrigger.next();
  }

  public readonly authenticated = toSignal(
    this.refreshTrigger.asObservable().pipe(
      switchMap(() => this.isAuthenticated())
    )
  );
}
