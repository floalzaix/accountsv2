import { Component, computed, inject } from '@angular/core';
import { TransactionsService } from '../trans.service';
import { TableModule } from 'primeng/table';
import { CategoriesService } from '../../categories/categories.service';
import { IdToNamePipe } from '../../shared/pipes/id-to-name-pipe';
import { ButtonModule } from 'primeng/button';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Transaction, TransactionSchema } from '../trans.model';
import { MessageService } from 'primeng/api';
import { ToastModule } from 'primeng/toast';
import { ErrorWrapper } from '../../shared/errors/error-wrapper';
import { KeyValuePipe } from '@angular/common';

@Component({
  selector: 'app-transactions-table',
  imports: [
    TableModule,
    IdToNamePipe,
    ButtonModule,
    ReactiveFormsModule,
    ToastModule,
    KeyValuePipe,
  ],
  templateUrl: './trans-table.component.html',
  styleUrl: './trans-table.component.css',
  providers: [MessageService],
})
export class TransactionsTable {
  //
  //   Interfaces
  //
  
  private readonly transactionsService = inject(TransactionsService);
  private readonly categoriesService = inject(CategoriesService);
  private readonly messageService = inject(MessageService);

  //
  //   Data
  //
  
  protected readonly transactions = this.transactionsService.transactions;
  protected readonly categoriesMap = this.categoriesService.categoriesMap;

  //
  //   Computed values
  //
  
  protected readonly tableRows = computed(() => {
    if (!this.transactions()) return [];

    this.buildEditTransactionFormArray(this.transactions()!);

    return this.transactions()?.map((transaction) => {
      return {
        ...transaction,
        state: "view"
      }
    })
  });

  //
  //   Forms
  //
  
  protected editTransactionForm = new FormGroup({});

  //
  //   Methods
  //

  private buildEditTransactionFormArray(transactions: Transaction[]) {
    const formGroups: { [key: string]: FormGroup } = {};

    for (const transaction of transactions) {
      if (!transaction.id) continue;

      const formGroup = new FormGroup({
        event_date: new FormControl<Date>(transaction.event_date, [Validators.required]),
        motive: new FormControl<string>(transaction.motive, [Validators.required, Validators.minLength(1), Validators.maxLength(255)]),
        to: new FormControl<string>(transaction.to, [Validators.minLength(1), Validators.maxLength(255)]),
        bank_date: new FormControl<Date>(transaction.bank_date, [Validators.required]),
        category1_id: new FormControl<string | null | undefined>(transaction.category1_id),
        category2_id: new FormControl<string | null | undefined>(transaction.category2_id),
        category3_id: new FormControl<string | null | undefined>(transaction.category3_id),
        amount: new FormControl<number>(transaction.amount, [Validators.required]),
      });
      
      formGroups[transaction.id] = formGroup;
    }

    this.editTransactionForm = new FormGroup(formGroups);
  }

  protected editTransaction(transaction: Transaction) {
    // Getting data from the form
    const transactionsData: { [key: string]: FormGroup } = this.editTransactionForm.controls;
    const transactionData = transactionsData[transaction.id!];

    // Validating the data
    if (!transactionData.valid) {
      this.messageService.add({
        severity: 'error',
        summary: 'Erreur',
        detail: 'Champs invalides !',
      });
      return;
    }

    // Preparing the edited transaction
    const editedTransaction = TransactionSchema.parse({
      ...transactionData.value,
      type: transaction.type,
      id: transaction.id,
    });

    // Updating the transaction
    this.transactionsService.updateTransaction(editedTransaction).subscribe({ 
      next: () => {
        this.messageService.add({
          severity: 'success',
          summary: 'Succès',
          detail: 'Transaction mise à jour avec succès !',
        });

        // Refreshing the transactions
        this.transactionsService.refresh();
      },
      error: (error) => {
        if (error instanceof ErrorWrapper) {
          this.messageService.add({
            severity: 'error',
            summary: error.userSafeTitle,
            detail: error.userSafeDescription,
            life: 7000,
          });
        }

        throw error;
      },
    });
  }

  protected deleteTransaction(transactionId: string) {
    this.transactionsService.deleteTransaction(transactionId).subscribe({
      next: () => {
        this.messageService.add({
          severity: 'success',
          summary: 'Succès',
          detail: 'Transaction supprimée avec succès !',
        });

        // Refreshing the transactions
        this.transactionsService.refresh();
      },
      error: (error) => {
        if (error instanceof ErrorWrapper) {
          this.messageService.add({
            severity: 'error',
            summary: 'Erreur',
            detail: error.error.message,
          });
        }

        throw error;
      },
    });
  }
}
