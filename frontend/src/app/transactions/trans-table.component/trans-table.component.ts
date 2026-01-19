import { Component, inject, signal } from '@angular/core';
import { TransactionsService } from '../trans.service';
import { Transaction } from '../trans.model';
import { toSignal } from '@angular/core/rxjs-interop';
import { TableModule } from 'primeng/table';

@Component({
  selector: 'app-transactions-table',
  imports: [
    TableModule,
  ],
  templateUrl: './trans-table.component.html',
  styleUrl: './trans-table.component.css',
})
export class TransactionsTable {
  //
  //   Interfaces
  //
  
  private readonly transactionsService = inject(TransactionsService);

  //
  //   Data
  //
  
  protected readonly transactions = toSignal(
    this.transactionsService.getAllTransactions()
  );
}
