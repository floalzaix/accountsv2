import { Component, inject, signal } from '@angular/core';
import { TransactionsService } from '../trans.service';
import { TableModule } from 'primeng/table';
import { CategoriesService } from '../../categories/categories.service';
import { IdToNamePipe } from '../../shared/pipes/id-to-name-pipe';
import { ButtonModule } from 'primeng/button';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-transactions-table',
  imports: [
    TableModule,
    IdToNamePipe,
    ButtonModule,
    ReactiveFormsModule,
  ],
  templateUrl: './trans-table.component.html',
  styleUrl: './trans-table.component.css',
})
export class TransactionsTable {
  //
  //   Interfaces
  //
  
  private readonly transactionsService = inject(TransactionsService);
  private readonly categoriesService = inject(CategoriesService);

  //
  //   Data
  //
  
  protected readonly transactions = this.transactionsService.transactions;
  protected readonly categories = this.categoriesService.categories;
  protected readonly categoriesMap = this.categoriesService.categoriesMap;

  //
  //   Forms
  //
  
  protected readonly editTransactionForm = new FormGroup({
    event_date: new FormControl<string>(""),
    motive: new FormControl<string>(""),
    to: new FormControl<string>(""),
    bank_date: new FormControl<string>(""),
    category1_id: new FormControl<string>(""),
    category2_id: new FormControl<string>(""),
    category3_id: new FormControl<string>(""),
    amount: new FormControl<number>(0),
  });

  //
  //   State machine
  //
  
  protected readonly state = signal<"view" | "edit" | "delete">("view");
}
