import { inject, Injectable } from '@angular/core';
import { AsyncHttpClient } from '../shared/services/async-http-client';
import { BehaviorSubject, Observable, switchMap } from 'rxjs';
import { OptionsService } from '../shared/services/options';
import { toSignal } from '@angular/core/rxjs-interop';

@Injectable({
  providedIn: 'root',
})
export class SummaryService {
  //
  //   Interfaces
  //
  
  private readonly client = inject(AsyncHttpClient);
  private readonly optionsService = inject(OptionsService);

  //
  //   Methods
  //
  
  /**
   * Gets the user's balance depending onn the year
   * and the transaction type.
   * 
   * @returns The balance of the user.
   */
  public getBalance(): Observable<number> {
    return this.client.get<number>(
      "/summary/balance",
      {
        "year": this.optionsService.year(),
        "trans_types": this.optionsService.multipleTypes(),
      }
    );
  }

  //
  //   Refreshable data
  //
  
  private readonly refreshTrigger = new BehaviorSubject<void>(undefined);

  public refresh(): void {
    this.refreshTrigger.next();
  }

  /**
   * The balance of the user. But can be refreshed
   * ussing the refresh() method of the service on
   * the same instance.
   */
  public balance = toSignal(
    this.refreshTrigger.asObservable().pipe(
      switchMap(() => this.getBalance())
    )
  );
}
