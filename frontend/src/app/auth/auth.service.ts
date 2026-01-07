import { inject, Injectable } from '@angular/core';
import { AsyncHttpClient } from '../shared/services/async-http-client';
import { User } from './user.model';
import { ValidationError } from '../shared/errors/validation-error';
import { ErrorWrapper } from '../shared/errors/error-wrapper';
import { map, Observable } from 'rxjs';
import { LoginResponse, LoginResponseSchema } from './login-response.model';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  //
  //   Interfaces
  //
  
  private readonly asyncHttpClient = inject(AsyncHttpClient);

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
        'Passwords do not match',
        'The passwords do not match',
        new ValidationError('Passwords do not match')
      );
    }

    //
    //   Preparing the observable
    //
    const observable = this.asyncHttpClient.post<User>({
      endpoint: '/auth/register',
      json: {
        email,
        password,
        pseudo,
      },
    });

    return observable;
  }

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
      endpoint: '/auth/login',
      json: {
        email,
        password,
      },
    }).pipe(
      map((response) => LoginResponseSchema.parse(response).user)
    );

    return observable;
  } 
}
