import { Component, inject } from '@angular/core';
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
    ButtonModule
  ],
  templateUrl: './trans-add-bar.component.html',
  styleUrl: './trans-add-bar.component.css',
  providers: [MessageService],
})
export class TransactionAddBar {
  //
  //   Interface
  //
  
  private readonly transactionsService = inject(TransactionsService);
  
  private readonly messageService = inject(MessageService);

  //
  //   Forms
  //
  
  public transactionAddForm = new FormGroup({
    event_date: new FormControl<Date | null>(null, [Validators.required]),
    motive: new FormControl<string>("", [Validators.required, Validators.minLength(1), Validators.maxLength(255)]),
    to: new FormControl<string>("", [Validators.required, Validators.minLength(1), Validators.maxLength(255)]),
    bank_date: new FormControl<Date | null>(null, [Validators.required]),
    category1: new FormControl<string | null>(null),
    category2: new FormControl<string | null>(null),
    category3: new FormControl<string | null>(null),
    type: new FormControl<string>("TO CHANGE LATER"),
    amount: new FormControl<number | null>(null, [Validators.required]),
  });

  //
  //   Methods
  //
  
  public addTransaction(): void {
    // TO DO
  }
}
