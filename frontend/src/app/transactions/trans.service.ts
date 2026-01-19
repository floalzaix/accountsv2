import { inject, Injectable } from '@angular/core';
import { map, Observable } from 'rxjs';
import { Transaction, TransactionSchema } from './trans.model';
import { AsyncHttpClient } from '../shared/services/async-http-client';

@Injectable({
  providedIn: 'root',
})
export class TransactionsService {
  //
  //   Interfaces
  //
  
  private readonly http = inject(AsyncHttpClient);

  //
  //   Methods
  //
  
  public getAllTransactions(): Observable<Transaction[]> {
    //
    //   Prepare the observable
    //
    const observable = this.http.get<object>("/transactions").pipe(
      map((response) => {
        console.log(response);
        if (response instanceof Array) {
          return response.map((item) => TransactionSchema.parse(item));
        }

        throw new Error("Invalid response format");
      }),
    );

    return observable;
  }
}
