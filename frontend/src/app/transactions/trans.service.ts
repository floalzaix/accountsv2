import { inject, Injectable } from '@angular/core';
import { BehaviorSubject, catchError, map, Observable, of, switchMap, tap } from 'rxjs';
import { Transaction, TransactionSchema } from './trans.model';
import { AsyncHttpClient } from '../shared/services/async-http-client';
import { toSignal } from '@angular/core/rxjs-interop';
import { OptionsService } from '../shared/services/options';

@Injectable({
  providedIn: 'root',
})
export class TransactionsService {
  //
  //   Interfaces
  //

  private readonly opionsService = inject(OptionsService);
  
  private readonly http = inject(AsyncHttpClient);

  //
  //   Methods
  //
  
  public getAllTransactions(): Observable<Transaction[]> {
    //
    //   Prepare the observable
    //
    const observable = this.http.get<object>(
      "/transactions",
      {
        "trans_type": this.opionsService.types(),
      }
    ).pipe(
      map((response) => {
        if (!(response instanceof Array)) {
          throw new TypeError("Invalid response format !")
        }

        // Sorting the transactions
        const transactions = response.map((item) => {
          return TransactionSchema.parse(item)
        }).sort((a, b) => {
          const event_date_diff = a.event_date.getTime() - b.event_date.getTime();
          if (event_date_diff !== 0) return event_date_diff;

          const bank_date_diff = a.bank_date.getTime() - b.bank_date.getTime();
          if (bank_date_diff !== 0) return bank_date_diff;

          const motive_diff = a.motive.localeCompare(b.motive);
          if (motive_diff !== 0) return motive_diff;

          const to_diff = a.to.localeCompare(b.to);
          return to_diff;
        });

        return transactions;
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
    });

    return observable;
  }

  public updateTransaction(transaction: Transaction): Observable<unknown> {
    //
    //   Preparing the params
    //
    
    if (transaction.category1_id == "null") {
      transaction.category1_id = null;
    }
    if (transaction.category2_id == "null") {
      transaction.category2_id = null;
    }
    if (transaction.category3_id == "null") {
      transaction.category3_id = null;
    }

    //
    //   Prepare the observable
    //
    const observable = this.http.put<object>({
      endpoint: "/transactions",
      json: transaction,
    });

    return observable;
  }

  public deleteTransaction(transactionId: string): Observable<unknown> {
    //
    //   Prepare the observable
    //
    const observable = this.http.delete<object>(`/transactions/${transactionId}`);

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
