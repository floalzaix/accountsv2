import { inject, Injectable } from '@angular/core';
import { BehaviorSubject, catchError, map, Observable, switchMap } from 'rxjs';
import { Transaction, TransactionSchema } from './trans.model';
import { AsyncHttpClient } from '../shared/services/async-http-client';
import { toSignal } from '@angular/core/rxjs-interop';

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
        if (response instanceof Array) {
          return response.map((item) => TransactionSchema.parse(item));
        }

        throw new Error("Invalid response format");
      }),
    );

    return observable;
  }

  public addTransaction(transaction: Transaction): Observable<unknown> {
    //
    //   Prepare the observable
    //
    const observable = this.http.post<object>({
      endpoint: "/transactions",
      json: transaction,
    }).pipe(
      catchError((error) => {
        console.error(error.error);
        throw error;
      }),
    );

    return observable;
  }

  //
  //   Refreshable data
  //

  private readonly refreshTrigger = new BehaviorSubject<void>(undefined);
  
  /**
   * The purpose of this section is to allow every component dependent
   * on the list of transaction to be refreshed thanks to the refreshed
   * method at first. Fo instance you have two components depending on the
   * list of transaction, you can call the refreshed method and both will
   * be refreshed.
   * 
   * @param callback The callback to call when the data is refreshed.
   */
  public refresh(): void {
    this.refreshTrigger.next();
  }

  // Transactions list
  public readonly transactions = toSignal(this.refreshTrigger.pipe(
    switchMap(() => this.getAllTransactions())
  ));
}
