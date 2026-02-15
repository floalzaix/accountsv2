import { Component, computed, inject, input } from '@angular/core';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { TransactionsService } from '../trans.service';
import { DatePickerModule } from 'primeng/datepicker';
import { FloatLabelModule } from 'primeng/floatlabel';
import { IconFieldModule } from 'primeng/iconfield';
import { InputIconModule } from 'primeng/inputicon';
import { InputTextModule } from 'primeng/inputtext';
import { InputNumberModule } from 'primeng/inputnumber';
import { ButtonModule } from 'primeng/button';
import { MessageService } from 'primeng/api';
import { TransactionSchema } from '../trans.model';
import { ErrorWrapper } from '../../shared/errors/error-wrapper';
import { ToastModule } from 'primeng/toast';
import { formatDate } from '../../shared/utils/other';
import { DetailsService } from '../../details/details-service';
import { SummaryService } from '../../summary/summary.service';
import { OptionsService } from '../../shared/services/options';

@Component({
  selector: 'app-transaction-add-bar',
  imports: [
    FormsModule,
    ReactiveFormsModule,
    DatePickerModule,
    FloatLabelModule,
    IconFieldModule,
    InputIconModule,
    InputTextModule,
    InputNumberModule,
    ButtonModule,
    ToastModule
  ],
  templateUrl: './trans-add-bar.component.html',
  styleUrl: './trans-add-bar.component.css',
  providers: [MessageService],
})
export class TransactionAddBar {
  //
  //   Interface
  //

  public readonly level1SelectedCategory = input<string | null>(null);
  public readonly level2SelectedCategory = input<string | null>(null);
  public readonly level3SelectedCategory = input<string | null>(null);

  private readonly transactionsService = inject(TransactionsService);
  private readonly detailsService = inject(DetailsService);
  private readonly summaryService = inject(SummaryService);
  private readonly messageService = inject(MessageService);
  private readonly optionsService = inject(OptionsService);

  //
  //   Computed values
  //
  
  protected readonly minDate = computed(() => new Date(this.optionsService.year()!, 0, 1));
  protected readonly maxDate = computed(() => new Date(this.optionsService.year()!, 11, 31));

  //
  //   Forms
  //
  
  public transactionAddForm = new FormGroup({
    event_date: new FormControl<Date | null>(null, [Validators.required]),
    motive: new FormControl<string>("", [Validators.required, Validators.minLength(1), Validators.maxLength(255)]),
    to: new FormControl<string>("", [Validators.required, Validators.minLength(1), Validators.maxLength(255)]),
    bank_date: new FormControl<Date | null>(null, [Validators.required]),
    amount: new FormControl<number | null>(null, [Validators.required]),
  });

  //
  //   Methods
  //
  
  public addTransaction(): void {
    // Validating the form
    if (this.transactionAddForm.invalid) {
      this.messageService.add({
        severity: 'error',
        summary: 'Erreur',
        detail: 'Champs invalides !',
      });

      return;
    }


    // Preparing hte transaction
    const transaction = TransactionSchema.parse(
      {
        ...this.transactionAddForm.value,
        event_date: formatDate(
          this.transactionAddForm.value?.event_date!
        ),
        bank_date: formatDate(
          this.transactionAddForm.value?.bank_date!
        ),
        type: this.optionsService.types(),
        category1_id: this.level1SelectedCategory(),
        category2_id: this.level2SelectedCategory(),
        category3_id: this.level3SelectedCategory(),
      }
    )

    // Adding the transaction
    this.transactionsService.addTransaction(transaction).subscribe({
      next: () => {
        this.messageService.add({
          severity: 'success',
          summary: 'Succès',
          detail: 'Transaction ajoutée avec succès !',
        });

        // Refreshing the transactions service to actualise the front
        this.transactionsService.refresh();
        this.detailsService.refresh();
        this.summaryService.refresh();
      },
      error: (error) => {
        if (error instanceof ErrorWrapper) {
          this.messageService.add({
            severity: 'error',
            summary: error.userSafeTitle,
            detail: error.userSafeDescription,
          });
        }

        throw error;
      },
    });
  }
}
